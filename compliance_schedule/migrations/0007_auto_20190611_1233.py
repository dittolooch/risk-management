# Generated by Django 2.2.1 on 2019-06-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_schedule', '0006_auto_20190611_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyitem',
            name='regulatory_guide',
            field=models.CharField(blank=True, default='N/A', max_length=250),
            preserve_default=False,
        ),
    ]
