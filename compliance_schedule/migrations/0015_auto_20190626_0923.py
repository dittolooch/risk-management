# Generated by Django 2.2.1 on 2019-06-26 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0014_auto_20190625_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='responsible',
            field=models.CharField(choices=[('Managing Director - GMY', 'Managing Director - GMY'), ('GM Banking & Wholesale', 'GM Banking & Wholesale'), ('GM Aggregation', 'GM Aggregation'), ('Group CFO', 'Group CFO'), ('Banking CFO / Company Sec', 'Banking CFO / Company Sec'), ('Chief Risk Officer', 'Chief Risk Officer'), ('Head of Technology and Operations', 'Head of Technology and Operations'), ('Managing Director - Finsure', 'Managing Director - Finsure'), ('Board', 'Board'), ('Compliance Officer - Finsure', 'Compliance Officer - Finsure'), ('Head of Operations - Betterchoice', 'Head of Operations - Betterchoice')], max_length=200),
        ),
    ]
