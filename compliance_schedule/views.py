from django.shortcuts import render, redirect
from .models import ScheduleItem, CompletionDate, PolicyItem, ReviewDate
from .forms import ItemForm, UpdateForm, PolicyForm, UpdatePolicyForm
from django.views import View
from monthdelta import monthdelta
from forms.views import BaseTableView
from dashboard.views import SharedNames

class UpdateView(View):
    template_path = "compliance_schedule/update.html"
    model = UpdateForm
    item = ScheduleItem
    date_model = CompletionDate

    def get(self, request, form_id):
        form = self.model(instance = self.item.objects.get(id=form_id))
        return render(request, self.template_path, {'submitted':False, 'form':form})
    def post(self, request, form_id):
        submitted = False
        instance =  self.item.objects.get(id=form_id)
        form = self.model(request.POST or None, instance = instance)
        if form.is_valid() and request.user.is_authenticated:
            completion_date = self.date_model()
            completion_date.completion_date = form.cleaned_data['completion_date']
            completion_date.submitter = request.user
            completion_date.schedule_item = instance
            completion_date.save()
            instance.status = "DONE"
            instance.due_date = completion_date.completion_date + monthdelta(instance.frequency)
            instance.save()
            # if temp_form.completion_date
            submitted = True
            request.method="GET"
            return redirect("compliance_schedule:viewCompliance")
        return render(request, self.template_path, {'submitted':submitted, 'form':form})

class UpdatePolicyView(UpdateView):
    model = UpdatePolicyForm
    item = PolicyItem
    date_model = ReviewDate
    def post(self, request, form_id):
        submitted = False
        instance =  self.item.objects.get(id=form_id)
        form = self.model(request.POST or None, instance = instance)
        if form.is_valid() and request.user.is_authenticated:
            review_date = self.date_model()
            review_date.review_date = form.cleaned_data['review_date']
            review_date.submitter = request.user
            review_date.policy_item = instance
            review_date.save()
            instance.status = "DONE"
            instance.due_date = review_date.review_date + monthdelta(instance.frequency)
            instance.save()
            submitted = True
            request.method="GET"
            return redirect("compliance_schedule:viewPolicy")
        return render(request, self.template_path, {'submitted':submitted, 'form':form})

class ItemView(View):
    template_path = "compliance_schedule/form.html"
    model = ItemForm
    title = "Compliance Schedule"
    def get(self, request):
        submitted = False
        form = self.model()
        context =  {"submitted":submitted,"form":form, 'title':self.title}
        return render(request,self.template_path, context)
    def post(self, request):
        submitted = False
        form = self.model(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            temp_form = form.save(commit=False)
            temp_form.save()
            submitted = True
            request.method="GET"
        context =  {"submitted":submitted,"form":form, 'title':self.title}
        return render(request,self.template_path, context)
class PolicyFormView(ItemView):
    model = PolicyForm
    title = "Policy Review Schedule"

class ComplianceTableView(BaseTableView):
    template_path = "compliance_schedule/compliance_schedule_table.html"
    model_names = [SharedNames.compliance_schedule_item]
    def _get_table_config(self):
        config = {}
        config[SharedNames.compliance_schedule_item.replace(' ','_').lower()] = {
        'visible_indices':[
            'due_date',
            'last_completion_date',
            'status',
            'compliance_requirement',
            'regulator',
            'responsible',
            'frequency',
            'action'
            ]}
        return config
class PolicyTableView(BaseTableView):
    template_path = "compliance_schedule/policy_review_table.html"
    model_names = [SharedNames.policy_review_item]
    def _get_table_config(self):
        config = {}
        config[SharedNames.policy_review_item.replace(' ','_').lower()] = {
        'visible_indices':[
            'due_date',
            'last_review_date',
            'status',
            'policy_type',
            'name',
            'application',
            'responsible',
            'frequency',
            'action'
            ]}
        return config
