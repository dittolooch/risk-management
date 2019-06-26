from django.core.management.base import BaseCommand, CommandError
from forms.models import RiskControl, RiskFactor
from django.utils import timezone
from dashboard.views import DashboardTopItem
class Command(BaseCommand):
    help = 'update the risk factor effectiveness and the corresponding risk factor effectiveness'
    def __risk_control_295(self):
        dashboard_top_item = DashboardTopItem("Complaint")
    	last_12m_count = dashboard_top_item.get_count_between(
    	                        dashboard_top_item.x_year_ago(1),
    	                        timezone.now()
    	                    )
    	previous_12m_count = dashboard_top_item.get_count_between(
    	                        dashboard_top_item.x_year_ago(2),
    	                        dashboard_top_item.x_year_ago(1)
    	                    )
        growth = int(last_12m_count / previous_12m_count * 100)

    def handle(self, *args, **options):
        pass
