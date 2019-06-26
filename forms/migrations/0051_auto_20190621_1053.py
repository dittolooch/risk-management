# Generated by Django 2.2.1 on 2019-06-21 02:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0050_auto_20190620_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='incident_report_ref',
            field=models.CharField(blank=True, help_text='e.g. PIR ref', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='never_recovered_amount',
            field=models.FloatField(blank=True, help_text='$', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='recovered_amount',
            field=models.FloatField(blank=True, help_text='$', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='transaction_amount',
            field=models.FloatField(help_text='$', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='unrecoverable_amount',
            field=models.FloatField(blank=True, help_text='$', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]