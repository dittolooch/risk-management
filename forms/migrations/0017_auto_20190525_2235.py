# Generated by Django 2.2.1 on 2019-05-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0016_auto_20190525_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='broker_business_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='relevant_customer_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='representative_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
