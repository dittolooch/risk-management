from django.shortcuts import render, redirect
from django.db import models
from django.db.models import Func, F, Sum, Count, Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from forms.models import *
from datetime import timedelta
from monthdelta import monthdelta
from operator import itemgetter
import json
from compliance_schedule.models import PolicyItem, ScheduleItem
####Helper functions, and classes
class SharedNames:
	label_business_unit = "business_unit"
	fraud = "Fraud"
	incident = "Breach and Incident"
	hindsight = "Hindsight Review"
	complaint = "Complaint and Dispute"
	banking = "Banking"
	risk_control = "Risk Control"
	risk_factor_add = "Risk Factor Add"
	risk_factor_edit = "Risk Factor Edit"
	wholesale = "Wholesale"
	aggregation = "Aggregation"
	compliance_schedule_item = "Compliance Schedule Item"
	policy_review_item = "Policy Schedule Item"

	all_names = [fraud, incident, hindsight, complaint]
	models = {
	    fraud:Fraud,
	    incident:Incident,
	    complaint:Complaint,
		hindsight:Hindsight,
		risk_control:RiskControl,
		risk_factor_add:RiskFactor,
		risk_factor_edit:RiskFactor,
		compliance_schedule_item:ScheduleItem,
		policy_review_item :PolicyItem
	}
	heatmap_ids = {
	    fraud:"{}_heatmap".format(fraud),
	    incident:"{}_heatmap".format(incident),
	    complaint:"{}_heatmap".format(complaint),
	    hindsight:"{}_heatmap".format(hindsight),
	}
	full_names = {
	    fraud:"Frauds",
	    incident:"Breaches & Incidents",
	    complaint:"Complaints & Disputes",
	    hindsight: "Hindsight Reviews"
	}
	business_units = [
	    banking, wholesale, aggregation
	]
class Month(Func):
	function = "EXTRACT"
	template = "%(function)s(MONTH from %(expressions)s)"
	output_field = models.IntegerField()

class Year(Func):
	function = "EXTRACT"
	template = "%(function)s(YEAR from %(expressions)s)"
	output_field = models.IntegerField()



def get_12m_fraud_amounts():
	fraud_amounts=  {'date':[], 'loss':[]}
	for i in range(24):
		filt = {
		'discovery_date__gte':timezone.now() + monthdelta(-1-i),
		'discovery_date__lte':timezone.now() + monthdelta(-1*i),
		}
		loss = Fraud.objects.filter(**filt).values('transaction_amount').aggregate(amounts=Sum(F('transaction_amount')))['amounts']
		fraud_amounts['date'].append(str(timezone.now().date() + monthdelta(-1*i)))
		fraud_amounts['loss'].append(loss if loss else 0)
	return fraud_amounts

def get_12m_rolling(bu,item):

	complaint_losses = {"date":[],"loss":[]}
	incident_losses = {"date":[],"loss":[]}

	for i in range(24):
		filt = {
		'discovery_date__gte':timezone.now() + monthdelta(-12-i),
		'discovery_date__lte':timezone.now() + monthdelta(-1*i),
		'business_unit':bu
		}
		if item=="loss_incurred":
			filt = {
			'loss_incurred_date__gte':timezone.now() + monthdelta(-12-i),
			'loss_incurred_date__lte':timezone.now() + monthdelta(-1*i),
			'business_unit':bu
			}

		loss = Complaint.objects.filter(**filt).values(
				"business_unit",
				item,
				).aggregate(
					total_loss=Sum(
								F(item)
							)
				)["total_loss"]
		complaint_losses['date'].append(str(timezone.now().date() + monthdelta(-1*i)))
		complaint_losses['loss'].append(loss if loss else 0)
	for i in range(24):
		filt = {
		'discovery_date__gte':timezone.now() + monthdelta(-12-i),
		'discovery_date__lte':timezone.now() + monthdelta(-1*i),
		'business_unit':bu
		}
		if item=="loss_incurred":
			filt = {
			'loss_incurred_date__gte':timezone.now() + monthdelta(-12-i),
			'loss_incurred_date__lte':timezone.now() + monthdelta(-1*i),
			'business_unit':bu
			}
		loss = Incident.objects.filter(**filt).values(
				"business_unit",
				item,
				).aggregate(
					total_loss=Sum(
								F(item)
							)
				)["total_loss"]
		incident_losses['date'].append(str(timezone.now().date() + monthdelta(-1*i)))
		incident_losses['loss'].append(loss if loss else 0)

	for index, loss in enumerate(complaint_losses['loss']):
		incident_losses['loss'][index] += loss
	return incident_losses
def get_fraud_related_losses(bu):
	substrings=  ["fraud","paywave"]
	condition = Q(root_cause__icontains=substrings[0]) | Q(root_cause__icontains=substrings[1])


	item = "loss_incurred"
	complaint_losses = {"date":[],"loss":[]}
	incident_losses = {"date":[],"loss":[]}
	for i in range(24):
		loss = Complaint.objects.filter(
			loss_incurred_date__gte=timezone.now() + monthdelta(-12-i),
			loss_incurred_date__lte=timezone.now() + monthdelta(-1*i),
			business_unit=bu
		).filter(condition).values(
				"business_unit",
				item,

				).aggregate(
					total_loss=Sum(
								F(item)
							)
				)["total_loss"]
		complaint_losses['date'].append(str(timezone.now().date() + monthdelta(-1*i)))
		complaint_losses['loss'].append(loss if loss else 0)
	for i in range(24):
		loss = Incident.objects.filter(
			loss_incurred_date__gte=timezone.now() + monthdelta(-12-i),
			loss_incurred_date__lte=timezone.now() + monthdelta(-1*i),
			business_unit=bu
		).filter(condition).values(
				"business_unit",
				item,

				).aggregate(
					total_loss=Sum(
								F(item)
							)
				)["total_loss"]
		incident_losses['date'].append(str(timezone.now().date() + monthdelta(-1*i)))
		incident_losses['loss'].append(loss if loss else 0)

	for index, loss in enumerate(complaint_losses['loss']):
		incident_losses['loss'][index] += loss
	return incident_losses
"""
Dashbaord Top Item Data:
[
	[
	<major_name:str>,
	<major_number:int/float>,
	<minor_name:str>,
	<minor_number:int/float>,
	]

]
"""
class DashboardTopItem:
	def __init__(self, model_name ,filters = {}):
		self.model = SharedNames.models[model_name]
		self.filter = filters
	@property
	def first_day_of_this_year(self):
	    return timezone.now().replace(month=1, day=1)
	@property
	def first_day_of_last_year(self):
	    return self.first_day_of_this_year + monthdelta(-12)
	@property
	def first_day_of_this_month(self):
	    return timezone.now().replace(day=1)
	@property
	def first_day_of_last_month(self):
		return self.first_day_of_this_month + monthdelta(-1)
	def x_year_ago(self, x):
	    return timezone.now().replace(year=timezone.now().year-x)
	def _get_count(self, after):
	    try:
	        return self.model.objects.filter(discovery_date__gte=after, **self.filter).count()
	    except:
	        return self.model.objects.filter(submitted_date__gte=after, **self.filter).count()

	def _get_sum(self, after, field_name):
		if field_name == "loss_incurred":
			filt = {
			'loss_incurred_date__gte':after
			}
		else:
			filt = {
			'discovery_date__gte':after
			}

		try:
		    total = self.model.objects.filter(**filt, **self.filter).aggregate(total = Sum(field_name))["total"]
		except:
		    total = self.model.objects.filter(submitted_date__gte=after, **self.filter).aggregate(total = Sum(field_name))["total"]

		if total:
		    return int(total)
		else:
		    return 0
	def get_count_between(self, start_date, end_date):
	    return self._get_count(after=start_date) - self._get_count(after=end_date)
	def get_sum_between(self, start_date, end_date, field_name):
	    return self._get_sum(after=start_date, field_name = field_name) -\
	            self._get_sum(after=end_date, field_name = field_name)
	def get_data_between(self, start_date, end_date, data_type="count",field_name = None):
		if data_type =="count":
			return self.get_count_between(start_date, end_date)
		else:
			return self.get_sum_between(start_date, end_date, field_name)

"""
StackedBarchart Data = {
	<str:lable>:{
		<str:business_unit_1>:<int:count>,
		<str:business_unit_2>: <int:count>,
		<str:business_unit_3>: <int:count>,
	},



}
"""
class StackedBarChart:
	def __init__(self, model_name, count_field=None, sum_field=None, sum_by_field=None):
		self.model = SharedNames.models[model_name]
		self.stacked_field = "business_unit"
		self.count_field = count_field
		self.sum_field = sum_field
		self.sum_by_field = sum_by_field
	def get_top_ten_count_field(self):
		data = list(self.model.objects.values(self.count_field).annotate(count=Count(self.count_field)).order_by('-count'))
		if len(data) > 10:
			return [x[self.count_field] for x in data[:10]]
		else:
			return [x[self.count_field] for x in data]
	def get_count_field_by_stacked_field(self):
		return list(self.model.objects.values(self.count_field,self.stacked_field).annotate(count=Count(self.count_field)).order_by("-count"))
	def get_top_ten_sum_field_by(self):
		result = {}
		filter= {"{}__gt".format(self.sum_field):0}
		for i in self.model.objects.filter(**filter).values(self.sum_field,self.sum_by_field):
			sum_by_field = i[self.sum_by_field]
			sum_field = i[self.sum_field]
			if sum_by_field in result:
				result[sum_by_field] += sum_field
			else:
				result[sum_by_field]= sum_field
		sorted_result = sorted(result.items(), key = lambda kv:kv[1], reverse=True)


		if len(sorted_result) > 10:
			return [x[0] for x in sorted_result[:10]]
		else:
			return [x[0] for x in sorted_result]
	def get_count_data(self):
		data = []
		for item in self.get_top_ten_count_field():


			sub_dict = {}
			for bu in SharedNames.business_units:
				filter = {self.count_field:item, self.stacked_field:bu}
				sub_dict[bu]=self.model.objects.filter(**filter).count()
			if self.count_field == "risk_factor":
				item = RiskFactor.objects.get(id=item).name
			data.append([item,sub_dict])
		return data
	def get_sum_data(self):
		data = []
		for item in self.get_top_ten_sum_field_by():
			sub_dict = {}
			for bu in SharedNames.business_units:
				filter = {self.sum_by_field:item, self.stacked_field:bu, "{}__gt".format(self.sum_field):0}
				sub_dict[bu]=self.model.objects.filter(**filter).aggregate(sum=Sum(self.sum_field))['sum']
				if not sub_dict[bu]:
					sub_dict[bu]=0
				else:
					sub_dict[bu] = round(sub_dict[bu],0)
			data.append([item,sub_dict])
		return data

"""
Barchart Data = {
	<str:business_unit_1>:[
		[<str:label_1>, <int:count>],
		[<str:label_2>, <int:count>],
		...
	],
	<str:business_unit_2>:[
		[<str:label_1>, <int:count>],
		[<str:label_2>, <int:count>],
		...
	],

}
"""
class BarChart:
	def __init__(self, model_name, count_field=None, sum_field=None, sum_by_field=None):
		self.model = SharedNames.models[model_name]
		self.count_field = count_field
		self.sum_field = sum_field
		self.sum_by_field = sum_by_field

	def get_top_ten_count_field(self, business_unit):
		filter = {SharedNames.label_business_unit:business_unit}
		data = list(self.model.objects.filter(**filter).values(self.count_field).annotate(count=Count(self.count_field)).order_by('-count'))
		if self.count_field == "risk_factor":

			if len(data) > 10:
				return [[RiskFactor.objects.get(id=x[self.count_field]).name, x["count"]] for x in data[:10]]
			else:
				return [[RiskFactor.objects.get(id=x[self.count_field]).name, x["count"]] for x in data]
		else:

			if len(data) > 10:
				return [[x[self.count_field], x["count"]] for x in data[:10]]
			else:
				return [[x[self.count_field], x["count"]] for x in data]
	def get_top_ten_sum_field(self, business_unit):
		result = {}
		filter= {"{}__gt".format(self.sum_field):0, SharedNames.label_business_unit:business_unit}
		for i in self.model.objects.filter(**filter).values(self.sum_field,self.sum_by_field):
			sum_by_field = i[self.sum_by_field]
			sum_field = i[self.sum_field]
			if sum_by_field in result:
				result[sum_by_field] += sum_field
			else:
				result[sum_by_field]= sum_field
		sorted_result = sorted(result.items(), key = lambda kv:round(kv[1],0), reverse=True)

		if len(sorted_result) > 10:
			return sorted_result[:10]
		else:
			return sorted_result
	def get_count_data(self):
		data = {}
		for bu in SharedNames.business_units:
			data[bu]= self.get_top_ten_count_field(business_unit = bu)
		return data
	def get_sum_data(self):
		data = {}
		for bu in SharedNames.business_units:
			data[bu]= self.get_top_ten_sum_field(business_unit = bu)
		return data
"""
Heatmap Data:
{
<str:heatmap_id>:{
		<str:business_unit>:{
			<int:this_year>:[
				[<date:date>, <int:count>],
				[<date:date>, <int:count>]...

			]
		}
	}
}

"""
class Heatmap:
	this_year = timezone.now().year
	last_year = this_year-1
	def __init__(self, model_name):
		self.model = SharedNames.models[model_name]
		self.heatmap_id = SharedNames.heatmap_ids[model_name]
		self.heatmap_fullname = SharedNames.full_names[model_name]
		self.model_name = model_name

	def get_data(self):
	    heatmap_data = {
	        self.heatmap_id:{
	            "chart_name":self.model_name,
	            SharedNames.banking:{self.this_year:[],self.last_year:[]},
	            SharedNames.wholesale:{self.this_year:[],self.last_year:[]},
	            SharedNames.aggregation:{self.this_year:[],self.last_year:[]},
	        }
	    }
	    try:
	        data_by_dates = list(self.model.objects.extra({'discovery_date' : "date(discovery_date)"}).values('discovery_date','business_unit').annotate(count=Count('discovery_date')).order_by("count"))
	    except:
	        data_by_dates = list(self.model.objects.extra({'discovery_date' : "date(discovery_date)"}).values('discovery_date').annotate(count=Count('discovery_date')).order_by("count"))

	    for com in data_by_dates:
	        if com["discovery_date"].year in [self.this_year, self.last_year]:
	            try:
	                heatmap_data[self.heatmap_id][com["business_unit"]][com["discovery_date"].year].append([str(com["discovery_date"]+timedelta(days=1)),com["count"]])
	            except:
	                heatmap_data[self.heatmap_id][SharedNames.banking][com["discovery_date"].year].append([str(com["discovery_date"]+timedelta(days=1)),com["count"]])
	    return heatmap_data

"""
Gauges Data:
[
{"business_unit":<str:bu>, "count":<int:count>},
{"business_unit":<str:bu>, "count":<int:count>},
]
"""
class Gauge:
	def __init__(self, model_name, filt):
		self.filter = filt
		self.model = SharedNames.models[model_name]
	def get_data(self):
		data = []
		data.append(
			{
				SharedNames.label_business_unit:"Group",
				"count":self.model.objects.filter(**self.filter).count()
			}
		)
		for bu in SharedNames.business_units:
			new_filter = {**self.filter,**{SharedNames.label_business_unit:bu}}

			data.append({
				SharedNames.label_business_unit:bu,
				"count":self.model.objects.filter(**new_filter).count()
			})
		return data


### Views start here

def handler404(request, exception, template_name=""):
	return render(request, "dashboard/error_404.html")
def handler500(request, template_name=""):
	return render(request, "dashboard/error_500.html")




@login_required
def incident(request):
	"""
	Dashboard top item
	"""

	dashboard_top_item = DashboardTopItem(SharedNames.incident)
	last_30_day_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.first_day_of_this_month,
	                        timezone.now()
	                    )
	previous_30_day_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.first_day_of_last_month,
	                        dashboard_top_item.first_day_of_this_month
	                    )
	last_12m_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.x_year_ago(1),
	                        timezone.now()
	                    )
	previous_12m_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.x_year_ago(2),
	                        dashboard_top_item.x_year_ago(1)
	                    )
	last_12m_losses = dashboard_top_item.get_sum_between(
	                        dashboard_top_item.x_year_ago(1),
	                        timezone.now(),
	                        "loss_incurred"
	                    )
	previous_12m_losses = dashboard_top_item.get_sum_between(
	                        dashboard_top_item.x_year_ago(2),
	                        dashboard_top_item.x_year_ago(1),
	                        "loss_incurred"
	                    )
	actual_loss_growth = 0 if previous_12m_losses ==0 else  (last_12m_losses / preivous_12m_losses-1)*100

	dashboard_top_data = [
	    [
	        "Last 12-Month Incidents",
	        last_12m_count,

	        (last_12m_count/previous_12m_count-1)*100
	    ],
	    [
	        "Last 12-Month Losses",
	        last_12m_losses,

	        actual_loss_growth,
	    ],
	]
	"""
	Heatmaps
	"""
	heatmap_data = Heatmap(model_name = SharedNames.incident).get_data()

	"""
	Bar Charts
	"""
	risk_factor_stacked_data = StackedBarChart(model_name = SharedNames.incident, count_field = "risk_factor").get_count_data()
	risk_factor_non_stacked_data = BarChart(model_name = SharedNames.incident, count_field = "risk_factor").get_count_data()
	category_stacked_data = StackedBarChart(model_name = SharedNames.incident, count_field = "root_cause").get_count_data()
	cateogry_non_stacked_data = BarChart(model_name = SharedNames.incident, count_field = "root_cause").get_count_data()
	bar_chart_data = {
		"risk_factor":{
			"stacked":risk_factor_stacked_data,
			"non_stacked":risk_factor_non_stacked_data
		},
		"root_cause":{
			"stacked":category_stacked_data,
			"non_stacked":cateogry_non_stacked_data

		}
	}

	"""
	Gauges Charts
	"""
	gauges_data = Gauge(model_name=SharedNames.incident, filt={"status":"Open"}).get_data()

	context = {
		"dashboard_top_data":dashboard_top_data,
		"heatmap_data":json.dumps(heatmap_data),
		"bar_chart_data":json.dumps(bar_chart_data),
		"gauges_data":gauges_data,
		"gauges_data_js":json.dumps(gauges_data),
	}
	return render(request, "dashboard/dashboard_incident.html", context)
@login_required
def complaint(request):
	"""
	Dashboard top item
	"""
	dashboard_top_item = DashboardTopItem(SharedNames.complaint)
	last_30_day_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.first_day_of_this_month,
	                        timezone.now()
	                    )
	previous_30_day_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.first_day_of_last_month,
	                        dashboard_top_item.first_day_of_this_month
	                    )
	last_12m_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.x_year_ago(1),
	                        timezone.now()
	                    )
	previous_12m_count = dashboard_top_item.get_count_between(
	                        dashboard_top_item.x_year_ago(2),
	                        dashboard_top_item.x_year_ago(1)
	                    )
	last_12m_losses = dashboard_top_item.get_sum_between(
	                        dashboard_top_item.x_year_ago(1),
	                        timezone.now(),
	                        "loss_incurred"
	                    )
	previous_12m_lossed = dashboard_top_item.get_sum_between(
	                        dashboard_top_item.x_year_ago(2),
	                        dashboard_top_item.x_year_ago(1),
	                        "loss_incurred"
	                    )
	loss_incurred_growth = 0 if previous_12m_lossed==0 else (last_12m_losses / previous_12m_lossed-1)*100
	total_potential_losses = dashboard_top_item.get_sum_between(
	                        dashboard_top_item.x_year_ago(10),
	                        timezone.now(),
	                        "potential_loss"
	                    )

	dashboard_top_data = [
	    [
	        "Last 12-Month Complaints",
	        last_12m_count,

	        (last_12m_count/previous_12m_count-1)*100
	    ],
	    [
	        "Last 12-Month Losses",
	        last_12m_losses,
	        loss_incurred_growth,
	    ],
	    [
	        "Total Potential Losses",
	        total_potential_losses,

	        0,
	    ],
		[
			"Open EDR - Banking",
			Complaint.objects.filter(resolution_scheme="EDR",status="Open",business_unit="Banking").count(),
			0
		],
		[
			"Open EDR - Wholesale",
			Complaint.objects.filter(resolution_scheme="EDR",status="Open",business_unit="Wholesale").count(),
			0
		],
		[
			"Open EDR - Aggregation",
			Complaint.objects.filter(resolution_scheme="EDR",status="Open",business_unit="Aggregation").count(),
			0
		],

	]
	for bu in SharedNames.business_units:
		dashboard_top_item = DashboardTopItem(SharedNames.complaint, {SharedNames.label_business_unit:bu})
		last_12m_count = dashboard_top_item.get_count_between(
		                        dashboard_top_item.x_year_ago(1),
		                        timezone.now()
		                    )
		previous_12m_count = dashboard_top_item.get_count_between(
		                        dashboard_top_item.x_year_ago(2),
		                        dashboard_top_item.x_year_ago(1)
		                    )
		last_12m_losses = dashboard_top_item.get_sum_between(
		                        dashboard_top_item.x_year_ago(1),
		                        timezone.now(),
		                        "loss_incurred"
		                    )
		previous_12m_losses = dashboard_top_item.get_sum_between(
		                        dashboard_top_item.x_year_ago(2),
		                        dashboard_top_item.x_year_ago(1),
		                        "loss_incurred"
		                    )
		dashboard_top_data.append(
		 [
 	        "Last 12M Complaints - {}".format(bu),
 	        last_12m_count,
 	        0 if previous_12m_count==0 else (last_12m_count/previous_12m_count-1)*100
 	    ]
		)
		dashboard_top_data.append(
		 [
 	        "Last 12M Losses - {}".format(bu),
 	        last_12m_losses,
 	        0 if previous_12m_losses==0 else (last_12m_losses/previous_12m_losses-1)*100
 	    ]
		)
	"""
	Heatmaps
	"""
	heatmap_data = Heatmap(model_name = SharedNames.complaint).get_data()

	"""
	Bar Charts
	"""
	risk_factor_stacked_data = StackedBarChart(model_name = SharedNames.complaint, count_field = "risk_factor").get_count_data()
	risk_factor_non_stacked_data = BarChart(model_name = SharedNames.complaint, count_field = "risk_factor").get_count_data()
	category_stacked_data = StackedBarChart(model_name = SharedNames.complaint, count_field = "category").get_count_data()
	cateogry_non_stacked_data = BarChart(model_name = SharedNames.complaint, count_field = "category").get_count_data()
	actual_loss_by_category_stacked_data = StackedBarChart(model_name = SharedNames.complaint, sum_field = "loss_incurred", sum_by_field="category").get_sum_data()
	actual_loss_by_category_non_stacked_data = BarChart(model_name = SharedNames.complaint,  sum_field = "loss_incurred", sum_by_field="category").get_sum_data()
	potential_loss_by_category_stacked_data = StackedBarChart(model_name = SharedNames.complaint, sum_field = "potential_loss", sum_by_field="category").get_sum_data()
	potential_loss_by_category_non_stacked_data = BarChart(model_name = SharedNames.complaint,  sum_field = "potential_loss", sum_by_field="category").get_sum_data()

	bar_chart_data = {
		"risk_factor":{
			"stacked":risk_factor_stacked_data,
			"non_stacked":risk_factor_non_stacked_data
		},
		"category":{
			"stacked":category_stacked_data,
			"non_stacked":cateogry_non_stacked_data

		},
		"actual_loss":{
			"stacked":actual_loss_by_category_stacked_data,
			"non_stacked":actual_loss_by_category_non_stacked_data
		},
		"potential_loss":{
			"stacked":potential_loss_by_category_stacked_data,
			"non_stacked":potential_loss_by_category_non_stacked_data
		}
	}

	"""
	Gauges Charts
	"""
	gauges_data = Gauge(model_name=SharedNames.complaint, filt={"status":"Open"}).get_data()

	context = {
		"dashboard_top_data":dashboard_top_data,
		"heatmap_data":json.dumps(heatmap_data),
		"bar_chart_data":json.dumps(bar_chart_data),
		"gauges_data":gauges_data,
		"gauges_data_js":json.dumps(gauges_data),
	}
	return render(request, "dashboard/dashboard_complaint.html", context)

@login_required
def index(request):
	"""
	Dashboard top item
	"""
	dashboard_top_data =[]
	breach_filters = [
		{
			'type':'count',
			"title":"12M Regs & Laws Breaches - {}".format(bu),
			"sum_field":None,
			"filter":{
				"risk_factor__name__icontains":"breach",
				SharedNames.label_business_unit:bu
			}
		} for bu in SharedNames.business_units
	]
	open_bicd_pot_loss_filters = [
		{
			'type':'sum',
			"title":"Open BICD Pot.Loss - {}".format(bu),
			"sum_field":"potential_loss",
			"filter":{
				'status':"Open",
				SharedNames.label_business_unit:bu
			}
		} for bu in SharedNames.business_units
	]
	combined_top_data_filters = breach_filters + open_bicd_pot_loss_filters
	for filter_data in combined_top_data_filters:
		data_type = filter_data['type']
		sum_field = filter_data['sum_field']
		title = filter_data['title']
		filt = filter_data['filter']
		complaint_top_item = DashboardTopItem(SharedNames.complaint, filters= filt )
		incident_top_item = DashboardTopItem(SharedNames.incident, filters= filt)
		last_12m = complaint_top_item.get_data_between(complaint_top_item.x_year_ago(1),timezone.now(), data_type, sum_field) + \
					incident_top_item.get_data_between(incident_top_item.x_year_ago(1),timezone.now(), data_type, sum_field)
		previous_12m = complaint_top_item.get_data_between(complaint_top_item.x_year_ago(2),complaint_top_item.x_year_ago(1), data_type, sum_field) + \
		incident_top_item.get_data_between(incident_top_item.x_year_ago(2),incident_top_item.x_year_ago(1), data_type, sum_field)
		if previous_12m==0:
			growth = 0
		else:
			growth = (last_12m/previous_12m-1)*100
		dashboard_top_data.append([title, last_12m, growth ])

	"""
	Heatmaps
	"""
	heatmap_data = Heatmap(model_name = SharedNames.fraud).get_data()
	"""
	Bar Charts - Monthly
	"""
	fraud_amounts = get_12m_fraud_amounts()
	wholesale_potential_losses = get_12m_rolling(SharedNames.wholesale, "potential_loss")
	aggregation_potential_losses = get_12m_rolling(SharedNames.aggregation, "potential_loss")
	wholesale_actual_losses = get_12m_rolling(SharedNames.wholesale,"loss_incurred")
	aggregation_actual_losses = get_12m_rolling(SharedNames.aggregation,"loss_incurred")
	banking_actual_losses = get_12m_rolling(SharedNames.banking,"loss_incurred")
	actual_losses = {
		SharedNames.banking:banking_actual_losses,
		SharedNames.wholesale:wholesale_actual_losses,
		SharedNames.aggregation:aggregation_actual_losses
	}
	fraud_losses = {
		SharedNames.banking:get_fraud_related_losses(SharedNames.banking),
		SharedNames.wholesale:get_fraud_related_losses(SharedNames.wholesale),
		SharedNames.aggregation:get_fraud_related_losses(SharedNames.aggregation),
	}
	potential_losses = {
		SharedNames.banking:get_12m_rolling(SharedNames.banking, "potential_loss"),
		SharedNames.wholesale:get_12m_rolling(SharedNames.wholesale, "potential_loss"),
		SharedNames.aggregation:get_12m_rolling(SharedNames.aggregation, "potential_loss"),
	}
	residual_risk_scores = {"y":[],"x":[]}

	for rf in RiskFactor.objects.all().values("current_residual_score",'name').order_by('-current_residual_score'):
		residual_risk_scores["y"].append(rf['name'])
		residual_risk_scores["x"].append(rf['current_residual_score'])

	"""
	Bar Charts - Stacked, by Risk Factor / Rot Cause
	"""

	def get_top_10_break_down(field_name):
		if field_name == "risk_factor":
			field_name_breakdown = []
			for risk_factor in RiskFactor.objects.all():
				risk_factor_name = risk_factor.name
				risk_factor_complant_count = risk_factor.complaints.count()
				risk_factor_incident_count = risk_factor.incidents.count()
				field_name_breakdown.append({
					"risk_factor":risk_factor_name,
					"complaint_count":risk_factor_complant_count,
					"incident_count":risk_factor_incident_count,
					"all_count": risk_factor_complant_count + risk_factor_incident_count
				})


			return sorted(field_name_breakdown, key=itemgetter('all_count'), reverse=True)[:10]


		total_counts=  {}
		model_objects_by_field_name = [
			list(Incident.objects.values(field_name).annotate(count=Count(field_name)).order_by('-count')),
			list(Complaint.objects.values(field_name).annotate(count=Count(field_name)).order_by('-count'))
		]
		for objects in model_objects_by_field_name:
			for instance in objects:
			    field_name_label = instance[field_name]
			    field_name_count = instance["count"]
			    if field_name_label in total_counts:
			        total_counts[field_name_label]+=field_name_count
			    else:
			        total_counts[field_name_label] = field_name_count

			object_count_by_field_name = sorted(total_counts.items(), key=lambda kv: kv[1], reverse=True)
			if len(object_count_by_field_name)>10:
			    object_count_by_field_name = object_count_by_field_name[:10]
		field_name_breakdown = []
		def get_count(objects, top_item):
		    for obj in objects:
		        if obj[field_name] == top_item:
		            return obj["count"]
		    return 0
		for field_name_instance in object_count_by_field_name:
		    top_item = field_name_instance[0]
		    complaint_count = get_count(model_objects_by_field_name[1], top_item)
		    incident_count = get_count(model_objects_by_field_name[0], top_item)
		    field_name_breakdown.append({
		        field_name:top_item,
		        "complaint_count":complaint_count,
		        "incident_count":incident_count
		    })
		return field_name_breakdown

	risk_factor_breakdown = get_top_10_break_down('risk_factor')
	root_cause_breakdown = get_top_10_break_down('root_cause')

	context = {
		"heatmap_data":json.dumps(heatmap_data),
		"wholesale_losses":json.dumps(wholesale_potential_losses),
		"aggregation_losses":json.dumps(aggregation_potential_losses),
		"actual_losses":json.dumps(actual_losses),
		"fraud_losses":json.dumps(fraud_losses),
		"dashboard_top_data":dashboard_top_data,
		'potential_losses':json.dumps(potential_losses),
		'fraud_amounts':json.dumps(fraud_amounts),
		"risk_factor_breakdown":json.dumps(risk_factor_breakdown),
		'root_cause_breakdown':json.dumps(root_cause_breakdown),
		'residual_risk_scores':json.dumps(residual_risk_scores)
	}
	return render(request, "dashboard/dashboard_index.html", context)
