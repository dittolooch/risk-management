from django.core.management.base import BaseCommand, CommandError
from compliance_schedule.models import ScheduleItem, PolicyItem
from django.utils import timezone
from monthdelta import monthdelta
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import threading
import datetime
from mysite.utils import BaseEmailSender

class OverDueEmailSender(BaseEmailSender):
    subject=  "BNK Support: Overdue Schedule Items"
    template_path = "compliance_schedule/email.html"
    def get_context(self):
        return {'form':self.kwargs['form'], 'title':self.kwargs['title']}

class Command(BaseCommand):
    help = 'check schedule item status'
    done = "DONE"
    pending = "PENDING"
    overdue = "OVERDUE"

    def _handle(self, model, title):
        today = timezone.now().date()
        set_overdues = model.objects.filter(due_date__lt = today, status=self.pending)
        if (set_overdues.count()):
            to_notify = list(set_overdues)
            set_overdues.update(status=self.overdue)
            OverDueEmailSender(to_compliance = True, receiver_list = [], form=to_notify, title = title).async_send()

        dones = model.objects.filter(due_date__lt = today+monthdelta(1), status=self.done)
        for done in dones:
            done.status = self.pending
            done.due_date = done.due_date + monthdelta(done.frequency)
            done.save()

    def handle(self, *args, **options):
        iterators = {"Policy Review Schedule":PolicyItem, "Compliance Schedule":ScheduleItem}
        for title, model in iterators.items():
            self._handle(model, title)
