# Generated by Django 2.2.1 on 2019-05-29 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0022_auto_20190528_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='received_date',
            new_name='discovery_date',
        ),
    ]
