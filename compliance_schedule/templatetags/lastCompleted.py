from django import template
import datetime
from compliance_schedule.models import ScheduleItem
register = template.Library()


@register.filter
def lastCompleted(item_id):
    if ScheduleItem.objects.get(id=item_id).completion_dates.count():
        return ScheduleItem.objects.get(id=item_id).completion_dates.all()[0].completion_date
    else:
        return ""
