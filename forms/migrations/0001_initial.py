# Generated by Django 2.2.1 on 2019-05-23 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_factor', models.IntegerField(choices=[(1, 'Inappropriate application of Credit Risk Policy'), (2, 'Credit concentration risk – portfolio credit concentration / aggregation '), (3, 'Strategic plan risk'), (4, 'Market risk – Interest Rate Risk in the Banking Book (IRRBB)'), (5, 'Minimum Liquid Holdings Requirement'), (6, 'Outsourcing Risk – Mortgage Brokers'), (7, 'Breach of the Tax Act'), (8, 'Fraudulent activity (Internal)'), (9, 'Fraudulent activity (External)'), (10, 'IT Security Risk'), (11, 'Fit & Proper'), (12, 'Key Person Risk'), (13, 'Breach of APRA administered legislation or regulation'), (14, 'Inappropriate Corporate Governance'), (15, 'Breach of any Group AFSL conditions'), (16, 'Breach of any Group ACL conditions - Banking'), (17, 'Breach of any Group ACL conditions - Aggregation'), (18, 'Breach of the Privacy Act'), (19, 'Breach of the AML/CTF Act'), (20, 'OSH'), (21, 'Liability claim not covered by indemnity insurance'), (22, 'Loss of records'), (23, 'Loss of Point of Representation (POR)'), (24, 'Denial of Access to Point of Representation (POR) '), (25, 'Loss of IT Communications'), (26, 'Data Risk'), (27, 'Loss of Key Outsourced Dependencies, including Offshoring'), (28, 'Account Opening / Fulfilment'), (29, 'Ineffective Risk and Compliance Framework '), (30, 'Project Risk'), (31, 'Capital Adequacy'), (32, 'Breach of NCCP Act'), (33, 'Complaints including Social Media'), (34, 'Theft including cyber extortion'), (35, 'Conflict of Interest'), (36, 'Competition Risk'), (37, 'Integration Risk'), (38, 'Mortgage management risk'), (39, 'Financial Reporting Framework'), (40, 'Contract Risk'), (41, 'Payment Processing Risk')])),
                ('business_unit', models.IntegerField(choices=[(1, 'Banking'), (2, 'Wholesale'), (3, 'Aggregation')])),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('discovery_date', models.DateTimeField()),
                ('incident_start_date', models.DateTimeField()),
                ('expected_resolution_date', models.DateTimeField()),
                ('closed_date', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Closed')])),
                ('incident_type', models.IntegerField(choices=[(1, 'Issue'), (2, 'Near Miss'), (3, 'Loss'), (4, 'Injury')])),
                ('description', models.TextField()),
                ('risk_category_1', models.TextField()),
                ('risk_category_2', models.TextField()),
                ('risk_category_3', models.TextField()),
                ('consequence', models.IntegerField(choices=[(1, '1. Significant'), (2, '2. Minor'), (3, '3. Moderate'), (4, '4. Major'), (5, '5. Catastrophic')])),
                ('reputation_consequence', models.IntegerField(choices=[(1, '1. Significant'), (2, '2. Minor'), (3, '3. Moderate'), (4, '4. Major'), (5, '5. Catastrophic')])),
                ('risk_owner', models.IntegerField(choices=[(1, 'Managing Director - GMY'), (2, 'GM Banking & Wholesale'), (3, 'GM Aggregation'), (4, 'Group CFO'), (5, 'Banking CFO / Company Sec'), (6, 'Chief Risk Officer'), (7, 'Head of Technology and Operations'), (8, 'Managing Director - Finsure')])),
                ('process', models.TextField()),
                ('activity', models.TextField()),
                ('major_system', models.CharField(choices=[(1, 'LoanWorks'), (2, 'Loan Kit'), (3, 'T24'), (4, 'Public Facing Website'), (5, 'Not Applicable')], max_length=160)),
                ('other_system', models.CharField(max_length=160)),
                ('monetary_impact', models.FloatField()),
                ('root_cause', models.IntegerField(choices=[(1, 'ATM Error'), (2, 'Broker difficult to contact'), (3, 'Core Banking System Error'), (4, 'Cyber Fraud'), (5, 'Delays due to broker'), (6, 'Delays due to lender'), (7, 'Disclosure docs not issued'), (8, 'Financial Fraud - Vigil'), (9, 'Fraud by Customer'), (10, 'Fraud by staff'), (11, 'Hardware Issue'), (12, 'Inadequate project governance'), (13, 'Incorrect assessment'), (14, 'Incorrect/inadequate advice'), (15, 'Incorrect/inadequate cost disclosure'), (16, 'Incorrect/inadequate product information'), (17, 'Incorrect/process disclosure'), (18, 'Lack of staff training'), (19, 'Loan Hardship/Postponement'), (20, 'Manual processing error'), (21, 'Misunderstanding of legislation'), (22, 'Outsourced Activity'), (23, 'Paywave - stolen card or dispute'), (24, 'Policies not followed'), (25, 'Software controls'), (26, 'Not Applicable')])),
                ('action_required_to_close', models.TextField()),
                ('person_responsible', models.CharField(max_length=160)),
                ('regulatory_reporting_required', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, 'Not Applicable')])),
                ('regulator', models.IntegerField(choices=[(1, 'APRA'), (2, 'ASIC Responsible Lending'), (3, 'Asic Other'), (4, 'AUSTRAC'), (5, 'ASX'), (6, 'Not Applicable')])),
                ('date_regulator_reported', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_incidents', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_incidents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated_date',),
            },
        ),
    ]