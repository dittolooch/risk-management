# Generated by Django 2.2.1 on 2019-06-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0007_auto_20190611_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyitem',
            name='application',
            field=models.CharField(choices=[('Banking, Wholesale and Aggregation', 'Banking, Wholesale and Aggregation'), ('Banking and Wholesale', 'Banking and Wholesale'), ('Banking only', 'Banking only'), ('Wholesale only', 'Wholesale only'), ('Aggregation only', 'Aggregation only'), ('Wholesale and Aggregation', 'Wholesale and Aggregation'), ('Banking and Aggregation', 'Banking and Aggregation'), ('Group Wide', 'Group Wide')], max_length=250),
        ),
    ]
