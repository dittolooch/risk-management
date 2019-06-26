
from django import template
from forms.models import RiskFactor
import datetime
register = template.Library()


@register.filter
def prettyHeader(header):

    return header.replace("_"," ").title()
