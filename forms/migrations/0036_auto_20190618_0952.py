# Generated by Django 2.2.1 on 2019-06-18 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0035_auto_20190618_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='risk_category_1',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='risk_category_2',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='risk_category_3',
        ),
    ]