# Generated by Django 2.2.1 on 2019-06-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0009_auto_20190611_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyitem',
            name='application',
            field=models.CharField(choices=[('Banking, Wholesale and Aggregation', 'Banking, Wholesale and Aggregation'), ('Banking only', 'Banking only'), ('Wholesale only', 'Wholesale only'), ('Aggregation only', 'Aggregation only'), ('Banking and Wholesale', 'Banking and Wholesale'), ('Wholesale and Aggregation', 'Wholesale and Aggregation'), ('Banking and Aggregation', 'Banking and Aggregation')], max_length=250),
        ),
    ]
