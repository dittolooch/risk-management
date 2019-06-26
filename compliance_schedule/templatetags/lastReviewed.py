from django import template
import datetime
from compliance_schedule.models import PolicyItem
register = template.Library()


@register.filter
def lastReviewed(item_id):
    if PolicyItem.objects.get(id=item_id).review_dates.count():
        return PolicyItem.objects.get(id=item_id).review_dates.all()[0].review_date
    else:
        return ""
