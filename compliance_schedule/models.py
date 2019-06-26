from django.db import models
from forms.choices import RISK_OWNER_CHOICES, APPLICATION_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from forms.choices import BU_CHOICES
from django.contrib.auth.models import User
REGULATOR_CHOICES = (
    ('BPAY','BPAY'),
    ('APRA','APRA'),
    ('ASX','ASX'),
    ('ASIC','ASIC'),
    ('AUSTRAC','AUSTRAC'),
    ('WORKSAFE','WORKSAFE'),
    ('ATO','ATO'),
    ('WORKPLACE GENDER EQUALITY AGENCY','WORKPLACE GENDER EQUALITY AGENCY'),
    ("N/A","N/A")
)
STATUS_CHOICES = (
('DONE','DONE'),
('PENDING','PENDING'),
('OVERDUE','OVERDUE'),
)
class ScheduleItem(models.Model):
    RISK_OWNER_CHOICES = (
        ('Managing Director - GMY','Managing Director - GMY'),
        ('GM Banking & Wholesale','GM Banking & Wholesale'),
        ('GM Aggregation','GM Aggregation'),
        ('Group CFO','Group CFO'),
        ('Banking CFO / Company Sec','Banking CFO / Company Sec'),
        ('Chief Risk Officer','Chief Risk Officer'),
        ('Head of Technology and Operations','Head of Technology and Operations'),
        ('Managing Director - Finsure','Managing Director - Finsure'),
        ('Board','Board'),
        ('Compliance Officer - Finsure', 'Compliance Officer - Finsure'),
        ('Head of Operations - Betterchoice', 'Head of Operations - Betterchoice'),

    )
    def __str__(self):
        return "{}:{}".format(self.compliance_requirement, self.responsible)
    due_date = models.DateTimeField()
    compliance_requirement = models.CharField(max_length=100)
    regulator = models.CharField(max_length=300, choices = REGULATOR_CHOICES)
    document_or_activity = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200,choices = RISK_OWNER_CHOICES)
    frequency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], help_text="0 to 24")
    business_unit = models.CharField(max_length=50, choices = BU_CHOICES)

    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='PENDING')
class CompletionDate(models.Model):
    class Meta:
        ordering = ['-completion_date']
    def __str__(self):
        return "{} {}".format(self.completion_date.date(), self.schedule_item)
    completion_date = models.DateTimeField(null=True)
    schedule_item = models.ForeignKey( ScheduleItem, on_delete = models.CASCADE, related_name = 'completion_dates')
    submitter = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'compliance_completion_dates')

class PolicyItem(models.Model):
    def __str__(self):
        return "{}_{}".format(self.policy_type, self.name)

    due_date = models.DateTimeField()
    policy_type = models.CharField(max_length=250)
    name =  models.CharField(max_length=250)
    regulators =  models.CharField(max_length=250)
    regulatory_guide =  models.CharField(max_length=250,blank = True)
    frequency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], help_text="0 to 24")

    status =  models.CharField(max_length=250, choices = STATUS_CHOICES)
    responsible = models.CharField(max_length=200,choices = RISK_OWNER_CHOICES)
    reviewer =  models.CharField(max_length=200,choices = RISK_OWNER_CHOICES)
    approval_body =  models.CharField(max_length=250, null = True, blank = True)
    application =  models.CharField(max_length=250, choices = APPLICATION_CHOICES)
    note =  models.TextField(blank = True)

class ReviewDate(models.Model):
    class Meta:
        ordering = ['-review_date']
    def __str__(self):
        return "{} {}".format(self.review_date.date(), self.policy_item)
    review_date = models.DateTimeField(null=True)
    policy_item = models.ForeignKey( PolicyItem, on_delete = models.CASCADE, related_name = 'review_dates')
    submitter = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'policy_reviewed_dates')


# Create your models here.
