# Generated by Django 2.2.1 on 2019-05-25 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0013_auto_20190525_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hindsight',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_hindsights', to=settings.AUTH_USER_MODEL),
        ),
    ]
