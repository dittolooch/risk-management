# Generated by Django 2.2.1 on 2019-06-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0011_auto_20190618_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='regulator',
            field=models.CharField(choices=[('BPAY', 'BPAY'), ('APRA', 'APRA'), ('ASX', 'ASX'), ('ASIC', 'ASIC'), ('AUSTRAC', 'AUSTRAC'), ('WORKSAFE', 'WORKSAFE'), ('ATO', 'ATO'), ('WORKPLACE GENDER EQUALITY AGENCY', 'WORKPLACE GENDER EQUALITY AGENCY')], max_length=300),
        ),
    ]
