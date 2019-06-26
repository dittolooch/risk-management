from django.contrib import admin
from .models import Incident, Complaint, Fraud, Hindsight, Question, Answer, Section, RiskFactor, RiskControl, RiskFactorDelta
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

admin.site.register(Hindsight)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Section)
@admin.register(RiskFactorDelta)
class RiskFactorDeltaAdmin(admin.ModelAdmin):
    list_display = (
        'risk_factor',
        'submitter',
        'residual_risk_rating',
    )

    ordering = list_display
@admin.register(RiskFactor)
class RiskFactorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'risk_category_1',
        'risk_category_2',
        'risk_category_3',
    )
    search_fields = ('name','risk_category_3')
    ordering = list_display
@admin.register(RiskControl)
class RiskControlAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'risk_factor',
        'operational_loss_event_tier_1_category',
        'operational_loss_event_tier_2_category',
        'control_score',
        'control_effectiveness',

    )
    search_fields = ('name','risk_factor')
    ordering = list_display

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_filter = (
        ('discovery_date', DateRangeFilter),
        ('submitted_date', DateRangeFilter),
    )
    list_display = (
        'discovery_date',
        'author',
        'updated_date',
        'closed_date',
        'status',
        'risk_owner',
        'root_cause',
        'risk_factor'
    )

    search_fields = ('risk_factor','root_cause')
    raw_id_fields = ('author',)
    data_hierarchy = 'submitted_date'
    ordering = (
        'status',
        'author',
        'risk_owner',
        'submitted_date',
        'updated_date',
        'root_cause',
        'risk_factor'
    )

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_filter = (
        ('discovery_date', DateRangeFilter),
         ('submitted_date', DateRangeFilter),
    )
    list_display = (
        'discovery_date',
        'business_unit',
        'updated_date',
        'closed_date',
        'status',
        'discovery_date',
        'root_cause',
        'risk_factor',
        'broker_name',
        'broker_business_name'
    )
    search_fields = (
        'root_cause',
        'risk_factor',
        'complainant_name',
        'broker_name',
        'broker_business_name'
    )
    raw_id_fields = ('author',)
    data_hierarchy = 'submitted_date'
    ordering = (
        'status',
        'author',
        'submitted_date',
        'updated_date'
    )

@admin.register(Fraud)
class FraudAdmin(admin.ModelAdmin):
    list_display = ('submitted_date', 'author', 'updated_date')
    list_filter = ( 'submitted_date', 'author')
    search_fields = ('result','comment')
    raw_id_fields = ('author',)
    data_hierarchy = 'submitted_date'
    ordering = ('author','submitted_date','updated_date')
