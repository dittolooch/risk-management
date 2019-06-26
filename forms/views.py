import json
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import IncidentForm, ComplaintForm, FraudForm, HindsightForm, RiskFactorAddForm, RiskFactorEditForm, RiskControlForm
from .models import Answer, Section, Incident, Fraud, Complaint, Hindsight, RiskFactor, RiskControl, RiskFactorDelta
from .choices import RISK_CATEGORIES, RISK_OWNER_EMAILS, LOSS_EVENT_CATEGORIES
from django.views import View
from mysite.utils import BaseEmailSender
import threading
import datetime
from django.contrib.auth.decorators import login_required
from dashboard.views import SharedNames
from django.core import serializers
from django.contrib.sites.models import Site
from django.http import HttpResponse


class SubmissionEmailSender(BaseEmailSender):
    subject = "BNK Support: Submission Received"
    template_path = "forms/email.html"
    def get_context(self):

        return {
            'domain':Site.objects.get_current().domain,
            'form_name':self.kwargs['form_name'],
            'pretty_form_name':self.kwargs['form_name'].replace("_"," ").title() if "pretty_form_name" not in self.kwargs else self.kwargs['pretty_form_name'],
            'form_id':self.kwargs['form_id'],
            'author_name':self.kwargs['author_name']
        }
class WizardSubmissionEmailSender(SubmissionEmailSender):
    template_path = "forms/wizard_email.html"
class EditEmailSender(SubmissionEmailSender):
    subject = "BNK Support: Update Received"


class BaseTableView(View):
    template_path = "forms/table_base.html"
    def _get_data(self):
        data = []
        for name in self.model_names:
            model = SharedNames.models[name]
            data.append({
            'id':name.replace(' ','_').lower(),
            'name':name,
            'data':serializers.serialize('python', model.objects.all(),use_natural_foreign_keys=True)
            })
        return data
    def _get_table_config(self):
        config = {}
        for name in self.model_names:
            config[name.replace(' ','_').lower()] = {'visible_indices':[0,1,2,-1]}
        return config
    def get(self, request):
        data = self._get_data()
        table_config = self._get_table_config()

        context = {
            'data':data,
            'table_config': json.dumps(table_config)
        }
        return render(request, self.template_path, context)
class SubmissionTableView(BaseTableView):

    model_names=  [SharedNames.incident, SharedNames.complaint, SharedNames.fraud, SharedNames.hindsight]
    def _get_table_config(self):
        config = {}
        config[SharedNames.incident.replace(' ','_').lower()] = {
        'visible_indices':[
            'discovery_date',
            'status',
            'risk_owner',
            'business_unit',
            'loss_incurred',
            'loss_incurred_date',
            'potential_loss',
            'root_cause',
            'risk_factor',
            'consequence',
            'action'
            ]}
        config[SharedNames.complaint.replace(' ','_').lower()] = {
        'visible_indices':[
            'discovery_date',
            'complainant_name',
            'broker_business_name',
            'broker_name',
            'loss_incurred',
            'loss_incurred_date',
            'potential_loss',
            'status',
            'business_unit',
            'resolution_scheme',
            'root_cause',
            'risk_factor',
            'action'
        ]}
        config[SharedNames.fraud.replace(' ','_').lower()] = {
        'visible_indices':[
            'submitted_date',
            'updated_date',
            'discovery_date',
            'result_date',
            'customer_account_number',
            'transaction_amount',
            'status',
            'action'
        ]}
        config[SharedNames.hindsight.replace(' ','_').lower()] = {
        'visible_indices':[
            'completed',
            'completion_date',
            'funder_policy',
            'loan_account',
            'borrower_name',
            'loan_approved_by',
            'action'
        ]}
        return config
class RiskFactorTableView(BaseTableView):
    template_path = "forms/table_risk_factors.html"

    model_names=  [SharedNames.risk_factor_edit, SharedNames.risk_control]
    def _get_table_config(self):
        config = {}
        config[SharedNames.risk_factor_edit.replace(' ','_').lower()] = {
        'visible_indices':[
            'name',
            'risk_owner',
            'application',
            'initial_likelihood',
            'control_effectiveness',
            'residual_likelihood',
            'max_consequence',
            'residual_risk_rating',
            'current_residual_score',
            'action'
            ]}
        config[SharedNames.risk_control.replace(' ','_').lower()] = {
        'visible_indices':[
            'name',
            'risk_factor',
            'description',
            'control_score',
            'control_effectiveness'
            'action'
        ]}

        return config
class BaseFormView(View):
    sections = None
    template_path = "forms/submission.html"
    incident = "breach_and_incident"
    fraud = "fraud"
    complaint = "complaint_and_dispute"
    hindsight = "hindsight_review"
    risk_factor_add = 'risk_factor_add'
    risk_factor_edit = 'risk_factor_edit'
    risk_control = "risk_control"
    name_to_model_form = {
        incident:IncidentForm,
        fraud:FraudForm,
        complaint:ComplaintForm,
        hindsight:HindsightForm,
        risk_factor_add:RiskFactorAddForm,
        risk_factor_edit:RiskFactorEditForm,
        risk_control:RiskControlForm
    }
    name_to_model = {
        incident:Incident,
        fraud:Fraud,
        complaint:Complaint,
        hindsight:Hindsight,
        risk_factor_add:RiskFactor,
        risk_factor_edit:RiskFactor,
        risk_control:RiskControl,
    }

    def _get_model_by(self,form_name):
        return self.name_to_model[form_name]
    def _get_model_form_by(self, form_name):
        return self.name_to_model_form[form_name]
    def _get_pretty_form_name(self, form_name):
        return form_name.replace("_"," ").title()
    def _create_context(self, *args, **kwargs):
        pass
    def _extract_email_and_name_from(self, request):
        author_email = request.user.email
        author_name = request.user.first_name.title()
        return author_email, author_name
    def get(self, request, form_name):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        pretty_form_name = self._get_pretty_form_name(form_name)
        form = form_class()
        sections = self.sections() if self.sections!=None else None
        context =  {'sections':sections,'html_form_name':form_name, "form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)
    def post(self, request, form_name):
        pass
class RiskFactorAddView(BaseFormView):
    template_path = 'forms/add_risk_factor.html'
    def post(self, request, form_name):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        form = form_class(request.POST)
        pretty_form_name = self._get_pretty_form_name(form_name)
        if form.is_valid() and request.user.is_authenticated:
            temp_form = form.save(commit=False)
            email, author_name = self._extract_email_and_name_from(request)
            temp_form.save()
            submitted = True
            request.method="GET"
            delta =  RiskFactorDelta()
            delta.reason_for_change = "First Submission"
            delta.change_date = timezone.now()
            delta.risk_factor = temp_form
            delta.residual_risk_rating = temp_form.residual_risk_rating
            delta.submitter = request.user
            delta.save()
        context =  {"form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)

class EditFormView(BaseFormView):
    template_path = "forms/edit.html"
    def get(self, request, form_name, form_id):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        pretty_form_name = self._get_pretty_form_name(form_name)
        model = self._get_model_by(form_name)
        instance = get_object_or_404(model, pk = form_id)

        form = form_class(instance= instance)
        context =  {"form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)
    def post(self, request, form_name, form_id):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        model = self._get_model_by(form_name)
        instance = get_object_or_404(model, pk = form_id)
        form = form_class(request.POST or None, instance = instance)

        pretty_form_name = self._get_pretty_form_name(form_name)
        if form.is_valid() and request.user.is_authenticated:
            temp_form = form.save(commit=False)
            print("valid!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(form.cleaned_data)
            submitted = True
            email, author_name = self._extract_email_and_name_from(request)
            temp_form.updater = request.user
            if "status" in form.cleaned_data and form.cleaned_data["status"] == "Closed":
                temp_form.closed_date = timezone.now()
            if "residual_risk_rating" in form.cleaned_data and form.cleaned_data['residual_risk_rating']!=instance.residual_risk_rating:
                temp_form.previous_residual_risk_rating = instance.residual_risk_rating
                temp_form.previous_residual_risk_rating_date = timezone.now()
            temp_form.save()

            request.method="GET"
            if 'risk_owner' in form.cleaned_data:
                receiver_list = [email, RISK_OWNER_EMAILS[form.cleaned_data['risk_owner']]]
            else:
                receiver_list = [email]
            email_sender = EditEmailSender(
                to_compliance = True,
                receiver_list = receiver_list,
                pretty_form_name = "<Update>: {}".format(pretty_form_name),
                form_name = form_name,
                form_id = temp_form.id,
                author_name = author_name
            )
            email_sender.async_send()
        context =  {"form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)

class RiskFactorEditView(EditFormView):
    template_path = 'forms/add_risk_factor.html'
    def get(self, request, form_name, form_id):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        pretty_form_name = self._get_pretty_form_name(form_name)
        model = self._get_model_by(form_name)
        instance = get_object_or_404(model, pk = form_id)
        form = form_class(
            instance = instance,
            initial = {
                'previous_residual_risk_rating':instance.residual_risk_rating,
                'reason_for_change':instance.deltas.all()[0].reason_for_change if instance.deltas.all().count()>0 else "" })

        context =  {"form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)
    def post(self, request, form_name, form_id):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        model = self._get_model_by(form_name)
        instance = get_object_or_404(model, pk = form_id)
        instance_residual_risk_rating = instance.residual_risk_rating
        form = form_class(request.POST or None, instance = instance)

        pretty_form_name = self._get_pretty_form_name(form_name)
        if form.is_valid() and request.user.is_authenticated:
            temp_form = form.save(commit=False)
            print("valid!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(form.cleaned_data)
            submitted = True
            email, author_name = self._extract_email_and_name_from(request)
            temp_form.save()
            if temp_form.residual_risk_rating != instance_residual_risk_rating:
                delta =  RiskFactorDelta()
                delta.reason_for_change = form.cleaned_data['reason_for_change']
                delta.change_date = timezone.now()
                delta.risk_factor = temp_form
                delta.residual_risk_rating = form.cleaned_data['residual_risk_rating']
                delta.submitter = request.user
                delta.save()


            request.method="GET"

        context =  {"form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)
class DefaultFormView(BaseFormView):
    def post(self, request, form_name):
        submitted = False
        form_class = self._get_model_form_by(form_name)
        form = form_class(request.POST)
        pretty_form_name = self._get_pretty_form_name(form_name)
        if form.is_valid() and request.user.is_authenticated:
            temp_form = form.save(commit=False)
            email, author_name = self._extract_email_and_name_from(request)
            temp_form.author = request.user
            temp_form.updater = request.user
            if "status" in form.cleaned_data and form.cleaned_data["status"] == "Closed":
                temp_form.closed_date = timezone.now()
            if 'risk_owner' in form.cleaned_data:
                receiver_list = [email, RISK_OWNER_EMAILS[form.cleaned_data['risk_owner']]]
            else:
                receiver_list = [email]
            temp_form.save()
            submitted = True
            request.method="GET"
            email_sender = SubmissionEmailSender(
            to_compliance=True,
            receiver_list=receiver_list,
            form_name = form_name,
            form_id=temp_form.id,
            author_name = author_name)
            email_sender.async_send()
        context =  {"form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)
class WizardFormView(BaseFormView):
    template_path = "forms/form_wizard.html"
    sections = Section.objects.all
    def post(self, request, form_name):
        sections = self.sections()
        pretty_form_name = self._get_pretty_form_name(form_name)
        form_class = self._get_model_form_by(form_name)
        form = form_class(request.POST)
        submitted = False
        data = json.dumps({'id':""})
        if form.is_valid() and request.user.is_authenticated:
            submitted = True
            completed = True
            temp_form = form.save(commit=False)
            email, author_name = self._extract_email_and_name_from(request)
            temp_form.author = request.user
            temp_form.updater = request.user
            temp_form.save()
            #save answers
            for field in form:
                field_key = field.auto_id[3:]
                if "section" in field.field.widget.attrs:
                    answer = Answer()
                    answer.hindsight = temp_form
                    answer.question_id = field.field.widget.attrs["question"]
                    if field.field.widget.attrs["answer_type"]=="Comment":
                        answer.comment = form.cleaned_data[field_key]
                    else:
                        answer.reviewed = form.cleaned_data[field_key]
                        if not answer.reviewed:
                            completed = False

                    answer.save()
            temp_form = Hindsight.objects.get(id= temp_form.id)
            if completed:
                temp_form.completed = completed
                temp_form.completion_date = timezone.now()
                temp_form.save()
                email_sender = WizardSubmissionEmailSender(
                to_compliance=True,
                receiver_list=[request.user.email],
                form_name = form_name,
                form_id=temp_form.id,
                author_name = request.user.first_name)
                email_sender.async_send()

            data =json.dumps({'id':temp_form.id})

        return HttpResponse(data, content_type='application/json')
class EditWizardView(BaseFormView):
    template_path = "forms/form_wizard.html"
    sections = Section.objects.all
    def get(self, request, form_name, form_id):
        sections = self.sections()
        submitted = False
        form_class = self._get_model_form_by(form_name)
        pretty_form_name = self._get_pretty_form_name(form_name)
        model = self._get_model_by(form_name)
        instance = get_object_or_404(model, pk = form_id)
        form = form_class(instance= instance)
        context =  {'form_id':form_id, 'html_form_name':form_name, 'sections':sections, "form_name":pretty_form_name,"submitted":submitted,"form":form, "risks":json.dumps(RISK_CATEGORIES), 'loss_event_categories':json.dumps(LOSS_EVENT_CATEGORIES)}
        return render(request,self.template_path, context)
    def post(self, request, form_name, form_id):
        sections = self.sections()
        form_class = self._get_model_form_by(form_name)
        model = self._get_model_by(form_name)
        instance = get_object_or_404(model, pk = form_id)
        form = form_class(request.POST or None, instance = instance)
        pretty_form_name = self._get_pretty_form_name(form_name)
        submitted = False
        if form.is_valid() and request.user.is_authenticated:
            submitted = True
            temp_form = form.save(commit=False)
            email, author_name = self._extract_email_and_name_from(request)
            temp_form.author = request.user
            temp_form.updater = request.user
            completed=True

            #save answers
            for field in form:
                field_key = field.auto_id[3:]
                if "section" in field.field.widget.attrs:
                    answer = Answer.objects.get(hindsight = instance, question_id =field.field.widget.attrs["question"] )
                    if field.field.widget.attrs["answer_type"]=="Comment":
                        answer.comment = form.cleaned_data[field_key]
                    else:
                        answer.reviewed = form.cleaned_data[field_key]
                        if not answer.reviewed:
                            completed = False
                    answer.save()
            if completed:
                temp_form.completed = completed
                temp_form.completion_date = timezone.now()

                email_sender = WizardSubmissionEmailSender(
                to_compliance=True,
                receiver_list=[request.user.email],
                form_name = form_name,
                form_id=temp_form.id,
                author_name = request.user.first_name
                )
                email_sender.async_send()
            temp_form.save()
            request.method="GET"
        data = json.dumps({'status':True})
        return HttpResponse(data, content_type='application/json')
