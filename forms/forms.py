
from django import forms
from .models import Incident, Complaint, Fraud, Section, Hindsight, RiskFactor, RiskControl
from .choices import HINDSIGHT_BOOLEAN_CHOICES, RISK_OWNER_EMAILS, RISK_RATING_CHOICES
class DateInput(forms.DateInput):
    input_type = 'date'

class HindsightForm(forms.ModelForm):
    class Meta:
        model = Hindsight
        fields = (
            'funder_policy',
            'borrower_name',
            'loan_account',
            'loan_approved_by'
        )
    def __init__(self, *args, **kwargs):
        super(HindsightForm, self).__init__(*args, **kwargs)
        for section in Section.objects.all():
            for question in section.questions.all():
                if question.answer_type != "Comment":
                    self.fields['{}_{}'.format(section.id, question.id)] = forms.ChoiceField(
                        choices=HINDSIGHT_BOOLEAN_CHOICES,
                        label=question.question_text,
                        widget=forms.Select(
                                attrs={
                                        'section':section.id,
                                        'question':question.id,
                                        'answer_type':question.answer_type
                                }
                        )
                    )

                else:
                    self.fields['{}_{}'.format(section.id, question.id)] = forms.CharField(
                        label=question.question_text,
                        widget = forms.Textarea(
                                attrs={
                                    'section':section.id,
                                    'question':question.id,
                                    'answer_type':question.answer_type
                                    }
                                )
                        )
                self.fields['{}_{}'.format(section.id, question.id)].required=False

class FraudForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FraudForm, self).__init__(*args, **kwargs)
        self.fields['advice_sender_email'].required = False
        self.fields['advice_sender_phone'].required = False
        self.fields['action_taken_other'].required = False
        self.fields['comment'].required = False
    class Meta:
        model = Fraud
        fields = (
            'discovery_date',
            'fraud_type',
            'discovery_hour',
            'discovery_minute',
            'advice_received_from',
            'advice_sender_name',
            'advice_sender_email',
            'advice_sender_phone',
            'customer_account_number',
            'transaction_amount',
            'recovered_amount',
            'unrecoverable_amount',
            'never_recovered_amount',
            'action_taken',
            'action_taken_other',
            'action_date',
            'action_hour',
            'action_minute',
            'action_result',
            'result_date',
            'result_hour',
            'result_minute',
            'staff_responsible',
            'suspicious_matter_reported',
            'comment',
            'status',
        )
        widgets = {
            'discovery_date':DateInput(),
            'action_date':DateInput(),
            'result_date':DateInput(),

        }

class IncidentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IncidentForm, self).__init__(*args, **kwargs)
        self.fields['expected_resolution_date'].required = False
        self.fields['date_regulator_reported'].required = False
        self.fields['expected_resolution_date'].required = False
        self.fields['loss_incurred_date'].required = False
        self.fields['other_system_affected'].required = False

    class Meta:
        model = Incident
        fields =('risk_factor',
                'business_unit',
                'discovery_date',
                'incident_start_date',
                'expected_resolution_date',
                'status',
                'incident_type',
                'description',
                'consequence',
                'risk_owner',
                'major_system_affected',
                'other_system_affected',
                'incident_report_ref',
                'loss_incurred',
                'loss_incurred_date',
                'potential_loss',
                'root_cause',
                'regulatory_reporting_required',
                'regulator',
                'date_regulator_reported',
                )
        widgets = {
            'expected_resolution_date': DateInput(),
            'discovery_date':DateInput(),
            'incident_start_date':DateInput(),
            'date_regulator_reported':DateInput(),
            'loss_incurred_date':DateInput()
        }
class RiskFactorAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RiskFactorAddForm, self).__init__(*args, **kwargs)


    class Meta:
        model = RiskFactor
        exclude = ('reason_for_change', )

class RiskFactorEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RiskFactorEditForm, self).__init__(*args, **kwargs)
        self.fields['previous_residual_risk_rating'] = forms.CharField(
            label="Previous residual risk rating",
            disabled=True,
            required=False
        )
        self.fields['reason_for_change'] = forms.CharField(label="Reason for change", widget=forms.Textarea, disabled=True, required=False)

    class Meta:
        model = RiskFactor
        fields = '__all__'


class RiskControlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RiskControlForm, self).__init__(*args, **kwargs)

    class Meta:
        model = RiskControl
        fields = '__all__'


class ComplaintForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['relevant_customer_number'].required = False
        self.fields['broker_business_name'].required = False
        self.fields['broker_name'].required = False
        self.fields['complainant_name'].required = False
        self.fields['category_other'].required = False
        self.fields['loss_incurred_date'].required = False

    class Meta:
        model = Complaint

        fields =(
            'discovery_date',
            'complaint_received_from',
            'relevant_customer_number',
            'broker_business_name',
            'broker_name',
            'complainant_name',
            'risk_factor',
            'business_unit',
            'status',
            'resolution_scheme',
            'category',
            'category_other',
            'litigation_commenced',
            'person_handling_complaint',
            'description',
            'amount_claimed_or_disputed',
            'payment_made_to_complainant',
            'loss_incurred',
            'loss_incurred_date',
            'potential_loss',
            'pursued_with_Ombudsmen',
            'root_cause',
        )
        labels = {"discovery_date":"Received date",}
        widgets = {
            'discovery_date': DateInput(),
            'loss_incurred_date':DateInput()
        }
