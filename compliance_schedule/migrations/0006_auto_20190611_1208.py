# Generated by Django 2.2.1 on 2019-06-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0005_auto_20190611_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyitem',
            name='application',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='policyitem',
            name='approval_body',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='policyitem',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='policyitem',
            name='policy_type',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='policyitem',
            name='regulators',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='policyitem',
            name='regulatory_guide',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='policyitem',
            name='status',
            field=models.CharField(choices=[('ON SCHEDULE', 'ON SCHEDULE'), ('OVERDUE', 'OVERDUE'), ('AHEAD OF SCHEDULE', 'AHEAD OF SCHEDULE')], max_length=250),
        ),
    ]
