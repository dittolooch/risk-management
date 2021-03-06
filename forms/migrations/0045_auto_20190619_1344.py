# Generated by Django 2.2.1 on 2019-06-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0044_auto_20190619_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskfactor',
            name='initial_risk_rating',
            field=models.CharField(choices=[('1. LOW', '1. LOW'), ('2. MODERATE', '2. MODERATE'), ('3. HIGH', '3. HIGH'), ('4. EXTREME', '4. EXTREME'), ('5. NEW', '5. NEW')], max_length=10),
        ),
        migrations.AlterField(
            model_name='riskfactor',
            name='previous_residual_risk_rating',
            field=models.CharField(choices=[('1. LOW', '1. LOW'), ('2. MODERATE', '2. MODERATE'), ('3. HIGH', '3. HIGH'), ('4. EXTREME', '4. EXTREME'), ('5. NEW', '5. NEW')], max_length=10),
        ),
        migrations.AlterField(
            model_name='riskfactor',
            name='residual_risk_rating',
            field=models.CharField(choices=[('1. LOW', '1. LOW'), ('2. MODERATE', '2. MODERATE'), ('3. HIGH', '3. HIGH'), ('4. EXTREME', '4. EXTREME'), ('5. NEW', '5. NEW')], max_length=10),
        ),
    ]
