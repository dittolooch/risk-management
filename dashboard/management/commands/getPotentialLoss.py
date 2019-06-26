from django.core.management.base import BaseCommand, CommandError
from dashboard.models import PotentialLoss
from dashboard.views import SharedNames, DashboardTopItem
from django.utils import timezone

class Command(BaseCommand):
    help = 'store potential loss to db for future ref'

    def handle(self, *args, **options):
        today = timezone.now().date()

        potential_loss = PotentialLoss.objects.filter(data_date__gte = today)
        if potential_loss.count() != 0:
            self.stdout.write(self.style.SUCCESS('Data is stored already'))
        else:
            potential_loss = PotentialLoss()
            for bu in SharedNames.business_units:
                filt = {"status":"Open", SharedNames.label_business_unit:bu}
                complaint_top_item = DashboardTopItem(SharedNames.complaint, filters= filt)
                incident_top_item = DashboardTopItem(SharedNames.incident, filters=  filt)
                last_12m_count = complaint_top_item.get_sum_between(complaint_top_item.x_year_ago(10),timezone.now(), field_name="potential_loss") + \
                incident_top_item.get_sum_between(incident_top_item.x_year_ago(10),timezone.now(),field_name="potential_loss")
                setattr(potential_loss,bu,last_12m_count)
                self.stdout.write(self.style.SUCCESS('{} {}'.format(bu, last_12m_count)))
            potential_loss.data_date = timezone.now()
            potential_loss.save()
