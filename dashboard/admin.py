from django.contrib import admin
from .models import PotentialLoss
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


@admin.register(PotentialLoss)
class PotentialLossAdmin(admin.ModelAdmin):
    list_filter = (
        ('data_date', DateRangeFilter),
    )
    list_display = ('data_date',"Banking","Wholesale","Aggregation")
    data_hierarchy = 'data_date'
    ordering = ('data_date','Banking','Wholesale','Aggregation')
