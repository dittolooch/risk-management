from django.contrib import admin
from .models import ScheduleItem, CompletionDate,PolicyItem , ReviewDate
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


admin.site.register(CompletionDate)

admin.site.register(ReviewDate)

@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_filter = (
        ('due_date', DateRangeFilter),
    )
    list_display = ('compliance_requirement',"regulator","responsible","frequency",'status', 'due_date')
    data_hierarchy = 'due_date'
    ordering = ('compliance_requirement',"regulator","responsible","frequency", 'due_date', 'status')
@admin.register(PolicyItem)
class PolicyItemAdmin(admin.ModelAdmin):
    list_filter = (
        ('due_date', DateRangeFilter),
    )
    list_display = ('policy_type','name','regulators','frequency','due_date','status','responsible','reviewer')
    ordering = ('policy_type','name','regulators','frequency','due_date','status','responsible','reviewer')
    data_hierarchy = 'due_date'
