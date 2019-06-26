# Generated by Django 2.2.1 on 2019-06-10 02:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regulatory_requirement', models.CharField(max_length=100)),
                ('regulator', models.CharField(choices=[('BPAY', 'BPAY'), ('APRA', 'APRA'), ('ASX', 'ASX'), ('ASIC', 'ASIC'), ('AUSTRAC', 'AUSTRAC'), ('BPAY', 'BPAY'), ('WORKSAFE', 'WORKSAFE'), ('ATO', 'ATO')], max_length=20)),
                ('document_or_activity', models.CharField(max_length=200)),
                ('responsible', models.CharField(choices=[('Managing Director - GMY', 'Managing Director - GMY'), ('GM Banking & Wholesale', 'GM Banking & Wholesale'), ('GM Aggregation', 'GM Aggregation'), ('Group CFO', 'Group CFO'), ('Banking CFO / Company Sec', 'Banking CFO / Company Sec'), ('Chief Risk Officer', 'Chief Risk Officer'), ('Head of Technology and Operations', 'Head of Technology and Operations'), ('Managing Director - Finsure', 'Managing Director - Finsure'), ('Board', 'Board')], max_length=200)),
                ('frequency', models.IntegerField(help_text='0 to 24', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CompletionDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completion_dates', to='compliance_schedule.ScheduleItem')),
            ],
        ),
    ]