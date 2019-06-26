# Generated by Django 2.2.1 on 2019-06-10 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0030_complaint_loss_incurred_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='risk_owner',
            field=models.CharField(choices=[('Managing Director - GMY', 'Managing Director - GMY'), ('GM Banking & Wholesale', 'GM Banking & Wholesale'), ('GM Aggregation', 'GM Aggregation'), ('Group CFO', 'Group CFO'), ('Banking CFO / Company Sec', 'Banking CFO / Company Sec'), ('Chief Risk Officer', 'Chief Risk Officer'), ('Head of Technology and Operations', 'Head of Technology and Operations'), ('Managing Director - Finsure', 'Managing Director - Finsure'), ('Board', 'Board')], max_length=200),
        ),
    ]
