# Generated by Django 2.2.1 on 2019-06-07 04:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190607_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialloss',
            name='data_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]