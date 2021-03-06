# Generated by Django 2.2.1 on 2019-05-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20190524_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='external_dispute_resolution_details',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='description',
            field=models.TextField(help_text='Related product, procedure followed, remedial action taken, improvement required,  details of investigation, external dispute resolution details etc...'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='loss_incurred',
            field=models.FloatField(help_text='Actual Payout by Group (Loss for Group) to resolve'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='potential_loss',
            field=models.FloatField(help_text='Potential Payout by Group (Loss for Group) to resolve'),
        ),
    ]
