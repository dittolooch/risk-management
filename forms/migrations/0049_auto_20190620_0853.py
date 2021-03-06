# Generated by Django 2.2.1 on 2019-06-20 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0048_auto_20190620_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskfactor',
            name='initial_risk_rating',
            field=models.CharField(blank=True, choices=[('1. LOW', '1. LOW'), ('2. MODERATE', '2. MODERATE'), ('3. HIGH', '3. HIGH'), ('4. EXTREME', '4. EXTREME'), ('5. NEW', '5. NEW')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riskfactor',
            name='previous_residual_risk_rating',
            field=models.CharField(blank=True, choices=[('1. LOW', '1. LOW'), ('2. MODERATE', '2. MODERATE'), ('3. HIGH', '3. HIGH'), ('4. EXTREME', '4. EXTREME'), ('5. NEW', '5. NEW')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riskfactor',
            name='residual_risk_rating',
            field=models.CharField(blank=True, choices=[('1. LOW', '1. LOW'), ('2. MODERATE', '2. MODERATE'), ('3. HIGH', '3. HIGH'), ('4. EXTREME', '4. EXTREME'), ('5. NEW', '5. NEW')], max_length=100, null=True),
        ),
    ]
