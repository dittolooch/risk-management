from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from .choices import *


class RiskFactor(models.Model):
    def natural_key(self):
        return self.name
    def __str__(self):
        return "{}".format(self.name)
    BOOLEAN_CHOICES = (
        ('YES','Yes'),
        ('NO','No')
    )
    LIKELIHOOD_CHOICES = (
        ('1. RARE', '1. Rare'),
        ('2. UNLIKELY', '2. Unlikely'),
        ('3. POSSIBLE', '3. Possible'),
        ('4. LIKELY', '4. Likely'),
        ('5. ALMOST CERTAIN', '5. Almost certain')
    )

    POTENTIAL_IMPACT_CHOICES = (
        ('Accounts not recorded correctly in CBS','Accounts not recorded correctly in CBS',),
        ('Breach of regulatory obligations','Breach of regulatory obligations',),
        ('Cost overuns','Cost overuns',),
        ('Credit loss','Credit loss',),
        ('Critical Business Operations (CBOs) not performed','Critical Business Operations (CBOs) not performed',),
        ('Damage to property','Damage to property',),
        ('Declared under FCS','Declared under FCS',),
        ('Delayed strategic outcomes','Delayed strategic outcomes',),
        ('Financial loss through legal action','Financial loss through legal action',),
        ('Inability to meet obligations','Inability to meet obligations',),
        ('Inability to raise further capital','Inability to raise further capital',),
        ('Insurance shortfall','Insurance shortfall',),
        ('Jail','Jail',),
        ('Loss earnings and reduction of capital','Loss earnings and reduction of capital',),
        ('Loss of ADI license','Loss of ADI license',),
        ('Loss of Credit License','Loss of Credit License',),
        ('Loss of customer data','Loss of customer data',),
        ('Loss of customer/deposit confidence','Loss of customer/deposit confidence',),
        ('Loss of customers','Loss of customers',),
        ('Loss of key staff','Loss of key staff',),
        ('Major Disruption','Major Disruption',),
        ('RAS breach','RAS breach',),
        ('Reduced Share Price','Reduced Share Price',),
        ('Regulatory breach','Regulatory breach',),
        ('Regulatory Fine','Regulatory Fine',),
        ('Regulatory investigation','Regulatory investigation',),
        ('Regulatory undertakings/infringement','Regulatory undertakings/infringement',),
        ('Reputational damage','Reputational damage',),
        ('RMF or RMS insufficient','RMF or RMS insufficient',),
        ('Staff injury or fatality','Staff injury or fatality',),
        ('Staff unable to discharge their duties','Staff unable to discharge their duties',),
        ('Temporary or short term operational fault','Temporary or short term operational fault',),

    )
    RISK_CATEGORY_ONE_CHOICES = ((x,x) for x in RISK_CATEGORIES.keys())
    all_level_2_lists = (list(x.keys()) for x in RISK_CATEGORIES.values())
    all_level_3_lists = [list(x.values()) for x in RISK_CATEGORIES.values()]
    all_level_2_risks = [item for sublist in all_level_2_lists for item in sublist]
    all_level_3_risks = [item for sublist in all_level_3_lists for item in sublist]
    all_level_3_risks = [item for sublist in all_level_3_risks for item in sublist]
    RISK_CATEGORY_TWO_CHOICES = ((x,x) for x in all_level_2_risks)
    RISK_CATEGORY_THREE_CHOICES = ((x,x) for x in all_level_3_risks)

    name = models.CharField(max_length =150)
    risk_owner = models.CharField(max_length=200,choices = RISK_OWNER_CHOICES)
    line_of_defense = models.IntegerField()
    risk_category_1 = models.CharField(max_length=150, choices =  RISK_CATEGORY_ONE_CHOICES)
    risk_category_2 = models.CharField(max_length=150, choices =  RISK_CATEGORY_TWO_CHOICES)
    risk_category_3 = models.CharField(max_length=150, choices =  RISK_CATEGORY_THREE_CHOICES)
    operation_risk = models.CharField(
                                max_length=3,
                                choices = BOOLEAN_CHOICES,
                                help_text = "(loss from failed processes, people and systems). APS 115 - include \
                                legal risk but exclude strategic and reputational (eg fraud, vendor, privacy, info security, cyber, DR/BCP)"
                            )
    application = models.CharField(max_length = 100, choices = APPLICATION_CHOICES)
    risk_description = models.TextField()
    material_risk = models.CharField(max_length=3, choices = BOOLEAN_CHOICES)
    RAS_metrics = models.TextField()
    RCSA_category = models.TextField(help_text = "Category of Process involved for Risk & Control self assessment (RCSA)")
    RCSA_process_activity = models.TextField(help_text = "Detailed Process Activities (RCSA)")
    RCSA_objective = models.TextField(help_text = "Objective of the Process (What do we want to achieve - why take the risk) (RCSA)")
    RCSA_inherent_risk = models.TextField(help_text = "Inherent Risks of the processes (RCSA) (Workflow study)")
    # work on getting the options in , and js
    RCSA_potential_impact_1 = models.CharField(choices = POTENTIAL_IMPACT_CHOICES, max_length=100, help_text = "Main potential impact to control -1 (RCSA)")
    RCSA_potential_impact_2 = models.CharField(choices = POTENTIAL_IMPACT_CHOICES, max_length=100, help_text = "Main potential impact to control -2 (RCSA)")
    initial_likelihood = models.CharField(max_length = 30, choices = LIKELIHOOD_CHOICES)
    financial_consequence = models.CharField(max_length=200,choices = CONSEQUENCE_CHOICES)
    reputational_consequence = models.CharField(max_length=200,choices = CONSEQUENCE_CHOICES)
    health_and_safety_consequence = models.CharField(max_length=200,choices = CONSEQUENCE_CHOICES)
    business_continuity_consequence = models.CharField(max_length=200,choices = CONSEQUENCE_CHOICES)
    compliance_and_legal_consequence = models.CharField(max_length=200,choices = CONSEQUENCE_CHOICES)
    initial_risk_rating = models.CharField(max_length = 100, choices = RISK_RATING_CHOICES, blank=True, null=True)
    control_effectiveness = models.IntegerField(default = 0)
    residual_likelihood = models.CharField(max_length = 30, choices = LIKELIHOOD_CHOICES, blank=True)
    residual_risk_rating = models.CharField(max_length = 100, choices = RISK_RATING_CHOICES, blank=True, null=True)
    current_residual_score = models.IntegerField()
    comment = models.TextField(blank=True)

class RiskFactorDelta(models.Model):
    change_date = models.DateTimeField(null = True, blank = True)
    risk_factor = models.ForeignKey(RiskFactor, on_delete= models.CASCADE, related_name = 'deltas')
    residual_risk_rating = models.CharField(max_length = 100, choices = RISK_RATING_CHOICES, blank=True, null=True)
    submitter = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'submitted_risk_factor_deltas')
    reason_for_change = models.TextField(blank=True)
    def __str__(self):
        return "{} {}".format(self.risk_factor, self.change_date)
    class Meta:
        ordering = ('-change_date',)
class RiskControl(models.Model):
    def natural_key(self):
        return self.name
    CATEGORY_ONE_CHOICES = ((x,x) for x in LOSS_EVENT_CATEGORIES.keys())
    all_level_2_lists = (list(x.keys()) for x in LOSS_EVENT_CATEGORIES.values())
    all_level_3_lists = [list(x.values()) for x in LOSS_EVENT_CATEGORIES.values()]
    all_level_2_risks = [item for sublist in all_level_2_lists for item in sublist]
    all_level_3_risks = [item for sublist in all_level_3_lists for item in sublist]
    all_level_3_risks = [item for sublist in all_level_3_risks for item in sublist]
    CATEGORY_TWO_CHOICES = ((x,x) for x in all_level_2_risks)
    CATEGORY_THREE_CHOICES = ((x,x) for x in all_level_3_risks)
    def __str__(self):
        return "{}".format(self.name)
    name = models.CharField(max_length = 200)
    risk_factor = models.ForeignKey(RiskFactor, on_delete= models.CASCADE, related_name = 'risk_controls')
    description = models.TextField()
    control_documents = models.CharField(max_length = 100)
    operational_loss_event_tier_1_category = models.CharField(max_length = 100, help_text="APS115", choices = CATEGORY_ONE_CHOICES)
    operational_loss_event_tier_2_category = models.CharField(max_length = 100, help_text="APS115",  choices = CATEGORY_TWO_CHOICES)
    operational_loss_event_activity = models.CharField(max_length = 100, help_text="APS115",  choices = CATEGORY_THREE_CHOICES)
    test_procedure_for_the_quarter = models.TextField()
    control_score_description = models.TextField()
    control_score = models.IntegerField()
    control_effectiveness = models.IntegerField(help_text = "%")
    potential_treatment_plans = models.TextField()



class Hindsight(models.Model):
    def __str__(self):
        return "loan_account_{}".format(self.loan_account)

    author = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'submitted_hindisights')
    updater = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'updated_hindsights')
    completed = models.BooleanField(default = False)
    completion_date = models.DateTimeField(blank = True, null = True)
    updated_date = models.DateTimeField(auto_now = True)
    funder_policy =models.CharField(max_length=200, choices = ADI_CHOICES)
    loan_account = models.CharField(max_length=20)
    borrower_name = models.CharField(max_length = 50)
    loan_approved_by = models.CharField(max_length=50, choices = LOAN_APPROVER_CHOICES)


class Section(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Question(models.Model):
    ANSWER_TYPE_CHOICES = (
    ('Multiple Choice', "Multiple Choice"),
    ('Comment', 'Comment')
    )
    def __str__(self):
        return "{}_{}: {}".format(self.section.id,self.id,self.question_text)
    question_text = models.CharField(max_length=300)
    section = models.ForeignKey( Section,
                                on_delete = models.CASCADE,
                                related_name = 'questions')
    answer_type = models.CharField(max_length=50, choices = ANSWER_TYPE_CHOICES)

class Answer(models.Model):
    def __str__(self):
        return "answer_to_question_{}_for_review_of_loan_account_{}".format(self.question.id, self.hindsight.loan_account)

    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name="answers")
    hindsight = models.ForeignKey(Hindsight, on_delete= models.CASCADE, related_name="answers")
    comment = models.TextField()
    reviewed = models.CharField(max_length=50, choices = HINDSIGHT_BOOLEAN_CHOICES)

class Fraud(models.Model):
    def __str__(self):
        return "{}_{}".format(self.submitted_date, self.author)
    ACTION_CHOICES = (
        ("Contacted Account Owner","Contacted Account Owner"),
        ("Recall Request","Recall Request"),
        ("Other","Other")
    )
    TYPE_CHOICES = (
    ('Romance Scam','Romance Scam'),
    ('Remote Software Hack','Remote Software Hack'),
    ('Porting','Porting'),
    ('Phishing','Phishing'),
    ('Money Mule','Money Mule'),
    ('Malware','Malware'),
    ('Invoice Fraud','Invoice Fraud'),
    ('Investment Scam','Investment Scam'),
    ("ID T'over","ID T'over"),
    ('Fraud Bank Transfer','Fraud Bank Transfer'),
    ('Email Hack','Email Hack'),
    ('Unknown','Unknown'),

    )
    discovery_date = models.DateTimeField() # use for top bar
    fraud_type = models.CharField(max_length=100, choices = TYPE_CHOICES)
    author = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'submitted_frauds')
    updater = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'updated_frauds')

    submitted_date = models.DateTimeField(default = timezone.now)
    updated_date = models.DateTimeField(auto_now = True)

    discovery_hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], help_text="0 to 24")
    discovery_minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)], help_text="0 to 60")
    advice_received_from = models.CharField(max_length=150, choices = ADI_CHOICES)
    advice_sender_name = models.CharField(max_length=50, blank=True, null=True)
    advice_sender_email = models.CharField(max_length=50, blank=True, null=True)
    advice_sender_phone = models.CharField(max_length=15, blank=True, null=True)
    customer_account_number = models.CharField(max_length=20,help_text="with BNK")
    transaction_amount = models.FloatField(help_text = "$", validators=[MinValueValidator(0)])
    recovered_amount = models.FloatField(help_text = "$",validators=[MinValueValidator(0)], blank=True, null = True)
    unrecoverable_amount = models.FloatField(help_text = "$",validators=[MinValueValidator(0)], blank=True, null = True)
    never_recovered_amount = models.FloatField(help_text = "$",validators=[MinValueValidator(0)], blank=True, null = True)
    action_taken = models.CharField(max_length=50, choices = ACTION_CHOICES)
    action_taken_other = models.TextField(help_text = "Enter the actions taken if Other was selected.")
    action_date = models.DateTimeField(null=True, blank=True)
    action_hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], help_text="0 to 24", null=True, blank=True)
    action_minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)], help_text="0 to 60",null=True, blank=True)
    action_result = models.TextField(null=True, blank=True)
    result_date = models.DateTimeField(null=True, blank=True)
    result_hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], help_text="0 to 24",null=True, blank=True)
    result_minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)], help_text="0 to 60",null=True, blank=True)
    staff_responsible = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'frauds_responsible')

    suspicious_matter_reported = models.CharField(max_length=5, choices = BOOLEAN_CHOICES)
    comment = models.TextField()
    status = models.CharField(max_length=10, choices = STATUS_CHOICES)


class Complaint(models.Model):
    class Meta:
        ordering = ('-discovery_date',)
    def get_absolute_url(self):
        return reverse('forms:edit',
        args=['complaint_and_dispute', self.id])
    def __str__(self):
        return "{}_{}".format(self.submitted_date, self.author)
    RESOLUTION_SCHEME_CHOICES = (
        ('IDR','Internal Dispute Resolution'),
        ('EDR','External Dispute Resolution')
    )
    CATEGORY_CHOICES = (
        ('General','General'),
        ('Accounts','Accounts'),
        ('EFT Transactions','EFT Transactions'),
        ('Privacy','Privacy'),
        ('Broker forgery','Broker forgery'),
        ('Broker mis-represented clients','Broker mis-represented clients'),
        ('Broker - bad advice','Broker - bad advice'),
        ('Broker - clawback dispute with client','Broker - clawback dispute with client'),
        ('Loan Hardship/Postponement','Loan Hardship/Postponement'),
        ('Loan Fees, Charges or Interest','Loan Fees, Charges or Interest'),
        ('Product Features','Product Features'),
        ('Joint customer dispute','Joint customer dispute'),
        ('Other','Other')
    )
    COMPLAINT_TYPE_CHOICES = (
        ("Customer","Customer"),
        ("Broker","Broker"),
        ("Licensee","Licensee"),
        ("General Public","General Public"),
        ("Other","Other")
    )

    discovery_date = models.DateTimeField()
    author = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'submitted_complaints')
    updater = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'updated_complaints')
    complaint_received_from = models.CharField(max_length=20, choices = COMPLAINT_TYPE_CHOICES)
    relevant_customer_number = models.CharField(max_length=20, blank=True)
    broker_business_name = models.CharField(max_length=100,blank=True)
    broker_name = models.CharField(max_length=100, blank=True, null=True)
    complainant_name = models.CharField(max_length=100,blank=True)

    submitted_date = models.DateTimeField(default = timezone.now)
    updated_date = models.DateTimeField(auto_now = True)

    risk_factor = models.ForeignKey(RiskFactor, null=True,on_delete = models.CASCADE, related_name="complaints")
    business_unit = models.CharField(max_length=200,choices = BU_CHOICES)
    status = models.CharField(max_length=200,choices = STATUS_CHOICES)
    resolution_scheme = models.CharField(max_length=100, choices = RESOLUTION_SCHEME_CHOICES)
    category = models.CharField(max_length=200, choices = CATEGORY_CHOICES)
    category_other = models.CharField(max_length=100, blank=True)
    litigation_commenced = models.CharField(max_length=5, choices = BOOLEAN_CHOICES)

    person_handling_complaint = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'handled_complaints')
    description = models.TextField(help_text = "Related product, procedure followed, remedial action taken, improvement required,  details of investigation, external dispute resolution details etc...")
    amount_claimed_or_disputed=  models.FloatField(validators=[MinValueValidator(0)])
    payment_made_to_complainant = models.FloatField(validators=[MinValueValidator(0)])
    loss_incurred= models.FloatField(validators=[MinValueValidator(0)],help_text="$ Actual Payout by Group (Loss for Group) to resolve")
    loss_incurred_date = models.DateTimeField(null=True, blank=True)
    potential_loss = models.FloatField(validators=[MinValueValidator(0)],help_text = "$ Potential Payout by Group (Loss for Group) to resolve")
    closed_date = models.DateTimeField(null=True, blank=True)
    pursued_with_Ombudsmen = models.CharField(max_length=10, choices =  BOOLEAN_CHOICES)
    root_cause = models.CharField(max_length=200,choices = ROOT_CAUSE_CHOICES)

class Incident(models.Model):
    def get_absolute_url(self):
        return reverse('forms:edit',
        args=['breach_and_incident', self.id])
    def __str__(self):
        return "{}_{}".format(self.submitted_date, self.author)
    class Meta:
        ordering = ('-discovery_date',)

    TYPE_CHOICES = (
        ("Issue","Issue"),
        ("Issue", "Near Miss"),
        ("Loss", "Loss"),
        ("Injury","Injury")
    )



    MAJOR_SYSTEM_CHOICES = (
        ("LoanWorks", "LoanWorks"),
        ("Loan Kit", "Loan Kit"),
        ("T24", "T24"),
        ('Insight','Insight'),
        ('Internet Banking','Internet Banking'),
        ('Phone Banking','Phone Banking'),
        ("Public Facing Website", "Public Facing Website"),
        ("Not Applicable", "Not Applicable")
    )
    REGULATORY_REPORTING_CHOICES=(
        ("Yes","Yes"),
        ("No","No"),
        ("Not Applicable","Not Applicable")
    )
    REGULATOR_CHOICES = (
        ("APRA", "APRA"),
        ("ASIC Responsible Lending", "ASIC Responsible Lending"),
        ("Asic Other", "Asic Other"),
        ("AUSTRAC", "AUSTRAC"),
        ("ASX", "ASX"),
        ("Not Applicable", "Not Applicable")
    )
    discovery_date = models.DateTimeField() # use discoveyr date for top bar
    risk_factor = models.ForeignKey(RiskFactor, null=True,on_delete = models.CASCADE, related_name="incidents")


    author = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'submitted_incidents')
    updater = models.ForeignKey( User,
                                on_delete = models.CASCADE,
                                related_name = 'updated_incidents')
    business_unit = models.CharField(max_length=200,choices = BU_CHOICES)
    submitted_date = models.DateTimeField(default = timezone.now)
    updated_date = models.DateTimeField(auto_now = True)

    incident_start_date = models.DateTimeField()
    expected_resolution_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=200,choices = STATUS_CHOICES)
    incident_type = models.CharField(max_length=200,choices = TYPE_CHOICES)
    description = models.TextField(help_text="Description, process, activity, persona responsible to close this incident etc...")

    consequence = models.CharField(max_length=200,choices = CONSEQUENCE_CHOICES)
    risk_owner = models.CharField(max_length=200,choices = RISK_OWNER_CHOICES)
    major_system_affected = models.CharField(max_length=160,choices = MAJOR_SYSTEM_CHOICES)
    other_system_affected = models.CharField(max_length=160, null=True, blank=True)
    incident_report_ref = models.CharField(max_length=50, null=True, blank = True, help_text = "e.g. PIR ref")
    loss_incurred= models.FloatField(help_text="$ dollar amount of loss incurred", validators=[MinValueValidator(0)])
    loss_incurred_date = models.DateTimeField( blank = True, null=True)
    potential_loss= models.FloatField(help_text="$ dollar amount of potential loss",validators=[MinValueValidator(0)])
    root_cause = models.CharField(max_length=200,choices = ROOT_CAUSE_CHOICES)
    regulatory_reporting_required = models.CharField(max_length=200,choices = REGULATORY_REPORTING_CHOICES)
    regulator = models.CharField(max_length=200,choices = REGULATOR_CHOICES, null=True, blank=True)
    date_regulator_reported = models.DateTimeField(null=True, blank=True)
