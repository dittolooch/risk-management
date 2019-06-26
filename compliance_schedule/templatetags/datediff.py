
from django import template
import datetime
register = template.Library()


@register.filter
def getdatediff(first_date, second_date):

    try:
        return abs((datetime.datetime.strptime(first_date,"%Y-%m-%d").date() - second_date.date()).days)
    except:
        return 0
