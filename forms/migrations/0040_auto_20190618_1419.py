# Generated by Django 2.2.1 on 2019-06-18 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0039_auto_20190618_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='risk_factor',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='risk_factor',
        ),
    ]