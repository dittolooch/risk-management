
from django import forms
from .models import ScheduleItem, PolicyItem

class DateInput(forms.DateInput):
    input_type = 'date'

class PolicyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PolicyForm, self).__init__(*args, **kwargs)
    class Meta:
        model = PolicyItem
        fields = '__all__'
        widgets = {
            'due_date': DateInput(),
        }

class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        # self.fields['expected_resolution_date'].required = False
# regulatory_requirement = models.CharField(max_length=100)
# regulator = models.CharField(max_length=20, choices = REGULATOR_CHOICES)
# document_or_activity = models.CharField(max_length=200)
# responsible = models.CharField(max_length=200,choices = RISK_OWNER_CHOICES)
# frequency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], help_text="0 to 24")
# due_date = models.DateTimeField()
    class Meta:
        model = ScheduleItem
        fields =(
        'business_unit',
        'compliance_requirement',
        'regulator',
        'document_or_activity',
        'responsible',
        'frequency',
        'due_date',
        )
        widgets = {
            'due_date': DateInput(),

        }
class UpdatePolicyForm(forms.ModelForm):
    review_date = forms.DateField(label="Review Date", widget=DateInput())
    def __init__(self, *args, **kwargs):
        super(UpdatePolicyForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            if field != "review_date" and field != "note":
                self.fields[field].disabled = True
    class Meta:
        model = PolicyItem
        fields = '__all__'
        widgets = {
            'review_date': DateInput(),
            'due_date':DateInput()
        }

class UpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            if field != "completion_date":
                self.fields[field].disabled = True


    completion_date = forms.DateField(label="Completion Date", widget=DateInput())
    class Meta:
        model = ScheduleItem
        fields = '__all__'
        widgets = {
            'completion_date': DateInput(),
            'due_date':DateInput()

        }
    # can use def clean_<any field name> to clean the value or raise validation errors
