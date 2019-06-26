# Generated by Django 2.2.1 on 2019-06-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0013_auto_20190625_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleitem',
            name='business_unit',
            field=models.CharField(choices=[('Banking', 'Banking'), ('Wholesale', 'Wholesale'), ('Aggregation', 'Aggregation')], default='Banking', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='regulator',
            field=models.CharField(choices=[('BPAY', 'BPAY'), ('APRA', 'APRA'), ('ASX', 'ASX'), ('ASIC', 'ASIC'), ('AUSTRAC', 'AUSTRAC'), ('WORKSAFE', 'WORKSAFE'), ('ATO', 'ATO'), ('WORKPLACE GENDER EQUALITY AGENCY', 'WORKPLACE GENDER EQUALITY AGENCY'), ('N/A', 'N/A')], max_length=300),
        ),
    ]
