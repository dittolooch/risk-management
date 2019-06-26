
from django import template
from forms.models import RiskFactor
import datetime
register = template.Library()


@register.filter
def maxConseq(risk_factor_id):
    risk_factor = RiskFactor.objects.get(id=risk_factor_id)
    max = 0
    max_conseq = None
    try:
        for field in risk_factor._meta.get_fields():
            if "consequence" in field.name:
                conseq_text = field.value_from_object(risk_factor)
                conseq_score = int(conseq_text[0])
                if conseq_score > max:
                    max = conseq_score
                    max_conseq = conseq_text
    except:
        max_conseq = "N/A"
    return max_conseq
