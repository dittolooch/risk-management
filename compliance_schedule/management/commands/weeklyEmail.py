from django.core.management.base import BaseCommand, CommandError
from compliance_schedule.models import ScheduleItem, PolicyItem

from django.utils import timezone
from monthdelta import monthdelta
from forms.models import Complaint, Incident
from dashboard.views import SharedNames
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from mysite.utils import BaseEmailSender
from .checkScheduleItem import OverDueEmailSender

class OpenBICDEmailSender(BaseEmailSender):
    subject=  "BNK Support: Open BICD Items"
    template_path = "compliance_schedule/open_email.html"
    def get_context(self):
        return {'form':self.kwargs['form'], 'title':self.kwargs['title']}


class Command(BaseCommand):
    overdue = "OVERDUE"
    def send_email_for_open_bicd(self):
        today = timezone.now().date()
        one_month_ago = today+monthdelta(-1)
        results =[]
        for bu in SharedNames.business_units:
            filt = {'status':'OPEN',SharedNames.label_business_unit:bu, 'discovery_date__lte':one_month_ago}
            complaints = list(Complaint.objects.filter(**filt))
            incidents = list(Incident.objects.filter(**filt))
            results.append(complaints+incidents)
        if len(results):
            OpenBICDEmailSender(to_compliance = True, receiver_list = [], form = results, title = "Open BICD Items").async_send()
    def send_overdue_compliance_email(self):
        overdues = ScheduleItem.objects.filter(status=self.overdue)
        if len(overdues):
            OverDueEmailSender(to_compliance = True, receiver_list = [], form=overdues, title = "Compliance Schedule").async_send()
        overdues_policy = PolicyItem.objects.filter(status=self.overdue)
        if len(overdues_policy):
            OverDueEmailSender(to_compliance = True, receiver_list = [], form=overdues_policy, title = "Policy Review Schedule").async_send()


    def handle(self, *args, **options):
        self.send_email_for_open_bicd()
        self.send_overdue_compliance_email()
