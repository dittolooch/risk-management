# Generated by Django 2.2.1 on 2019-06-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0008_auto_20190611_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyitem',
            name='status',
            field=models.CharField(choices=[('DONE', 'DONE'), ('PENDING', 'PENDING'), ('OVERDUE', 'OVERDUE')], max_length=250),
        ),
    ]
