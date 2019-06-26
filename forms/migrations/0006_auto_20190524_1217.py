# Generated by Django 2.2.1 on 2019-05-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20190524_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='business_unit',
            field=models.CharField(choices=[('Banking', 'Banking'), ('Wholesale', 'Wholesale'), ('Aggregation', 'Aggregation')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='consequence',
            field=models.CharField(choices=[('1. Significant', '1. Significant'), ('2. Minor', '2. Minor'), ('3. Moderate', '3. Moderate'), ('3. Moderate', '4. Major'), ('5. Catastrophic', '5. Catastrophic')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_type',
            field=models.CharField(choices=[('Issue', 'Issue'), ('Issue', 'Near Miss'), ('Loss', 'Loss'), ('Injury', 'Injury')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='regulator',
            field=models.CharField(choices=[('APRA', 'APRA'), ('ASIC Responsible Lending', 'ASIC Responsible Lending'), ('Asic Other', 'Asic Other'), ('AUSTRAC', 'AUSTRAC'), ('ASX', 'ASX'), ('Not Applicable', 'Not Applicable')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='regulatory_reporting_required',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Applicable', 'Not Applicable')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='reputation_consequence',
            field=models.CharField(choices=[('1. Significant', '1. Significant'), ('2. Minor', '2. Minor'), ('3. Moderate', '3. Moderate'), ('3. Moderate', '4. Major'), ('5. Catastrophic', '5. Catastrophic')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='risk_factor',
            field=models.CharField(choices=[('Inappropriate application of Credit Risk Policy', 'Inappropriate application of Credit Risk Policy'), ('Credit concentration risk – portfolio credit concentration / aggregation ', 'Credit concentration risk – portfolio credit concentration / aggregation '), ('Strategic plan risk', 'Strategic plan risk'), ('Market risk – Interest Rate Risk in the Banking Book (IRRBB)', 'Market risk – Interest Rate Risk in the Banking Book (IRRBB)'), ('Minimum Liquid Holdings Requirement', 'Minimum Liquid Holdings Requirement'), ('Outsourcing Risk – Mortgage Brokers', 'Outsourcing Risk – Mortgage Brokers'), ('Breach of the Tax Act', 'Breach of the Tax Act'), ('Fraudulent activity (Internal)', 'Fraudulent activity (Internal)'), ('Fraudulent activity (External)', 'Fraudulent activity (External)'), ('IT Security Risk', 'IT Security Risk'), ('Fit & Proper', 'Fit & Proper'), ('Key Person Risk', 'Key Person Risk'), ('Breach of APRA administered legislation or regulation', 'Breach of APRA administered legislation or regulation'), ('Inappropriate Corporate Governance', 'Inappropriate Corporate Governance'), ('Breach of any Group AFSL conditions', 'Breach of any Group AFSL conditions'), ('Breach of any Group ACL conditions - Banking', 'Breach of any Group ACL conditions - Banking'), ('Breach of any Group ACL conditions - Aggregation', 'Breach of any Group ACL conditions - Aggregation'), ('Breach of the Privacy Act', 'Breach of the Privacy Act'), ('Breach of the AML/CTF Act', 'Breach of the AML/CTF Act'), ('OSH', 'OSH'), ('Liability claim not covered by indemnity insurance', 'Liability claim not covered by indemnity insurance'), ('Loss of records', 'Loss of records'), ('Loss of Point of Representation (POR)', 'Loss of Point of Representation (POR)'), ('Denial of Access to Point of Representation (POR) ', 'Denial of Access to Point of Representation (POR) '), ('Loss of IT Communications', 'Loss of IT Communications'), ('Data Risk', 'Data Risk'), ('Loss of Key Outsourced Dependencies, including Offshoring', 'Loss of Key Outsourced Dependencies, including Offshoring'), ('Account Opening / Fulfilment', 'Account Opening / Fulfilment'), ('Ineffective Risk and Compliance Framework ', 'Ineffective Risk and Compliance Framework '), ('Project Risk', 'Project Risk'), ('Capital Adequacy', 'Capital Adequacy'), ('Breach of NCCP Act', 'Breach of NCCP Act'), ('Complaints including Social Media', 'Complaints including Social Media'), ('Theft including cyber extortion', 'Theft including cyber extortion'), ('Conflict of Interest', 'Conflict of Interest'), ('Competition Risk', 'Competition Risk'), ('Integration Risk', 'Integration Risk'), ('Mortgage management risk', 'Mortgage management risk'), ('Financial Reporting Framework', 'Financial Reporting Framework'), ('Contract Risk', 'Contract Risk'), ('Payment Processing Risk', 'Payment Processing Risk')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='risk_owner',
            field=models.CharField(choices=[('Managing Director - GMY', 'Managing Director - GMY'), ('GM Banking & Wholesale', 'GM Banking & Wholesale'), ('GM Aggregation', 'GM Aggregation'), ('Group CFO', 'Group CFO'), ('Banking CFO / Company Sec', 'Banking CFO / Company Sec'), ('Chief Risk Officer', 'Chief Risk Officer'), ('Head of Technology and Operations', 'Head of Technology and Operations'), ('Managing Director - Finsure', 'Managing Director - Finsure')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='root_cause',
            field=models.CharField(choices=[('ATM Error', 'ATM Error'), ('Broker difficult to contact', 'Broker difficult to contact'), ('Core Banking System Error', 'Core Banking System Error'), ('Cyber Fraud', 'Cyber Fraud'), ('Delays due to broker', 'Delays due to broker'), ('Delays due to lender', 'Delays due to lender'), ('Disclosure docs not issued', 'Disclosure docs not issued'), ('Financial Fraud - Vigil', 'Financial Fraud - Vigil'), ('Fraud by Customer', 'Fraud by Customer'), ('Fraud by staff', 'Fraud by staff'), ('Hardware Issue', 'Hardware Issue'), ('Inadequate project governance', 'Inadequate project governance'), ('Incorrect assessment', 'Incorrect assessment'), ('Incorrect/inadequate advice', 'Incorrect/inadequate advice'), ('Incorrect/inadequate cost disclosure', 'Incorrect/inadequate cost disclosure'), ('Incorrect/inadequate product information', 'Incorrect/inadequate product information'), ('Incorrect/process disclosure', 'Incorrect/process disclosure'), ('Lack of staff training', 'Lack of staff training'), ('Loan Hardship/Postponement', 'Loan Hardship/Postponement'), ('Manual processing error', 'Manual processing error'), ('Misunderstanding of legislation', 'Misunderstanding of legislation'), ('Outsourced Activity', 'Outsourced Activity'), ('Paywave - stolen card or dispute', 'Paywave - stolen card or dispute'), ('Policies not followed', 'Policies not followed'), ('Software controls', 'Software controls'), ('Not Applicable', 'Not Applicable')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=200),
        ),
    ]
