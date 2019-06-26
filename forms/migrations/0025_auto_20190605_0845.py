# Generated by Django 2.2.1 on 2019-06-05 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0024_auto_20190529_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='root_cause',
            field=models.CharField(choices=[('ATM Error', 'ATM Error'), ('Broker difficult to contact', 'Broker difficult to contact'), ('Core Banking System Error', 'Core Banking System Error'), ('Cyber Fraud', 'Cyber Fraud'), ('Delays due to broker', 'Delays due to broker'), ('Delays due to lender', 'Delays due to lender'), ('Disclosure docs not issued', 'Disclosure docs not issued'), ('Financial Fraud - Vigil', 'Financial Fraud - Vigil'), ('Fraud by Customer', 'Fraud by Customer'), ('Fraud by staff', 'Fraud by staff'), ('Fraud by representative', 'Fraud by representative'), ('Hardware Issue', 'Hardware Issue'), ('Inadequate project governance', 'Inadequate project governance'), ('Incorrect assessment', 'Incorrect assessment'), ('Incorrect/inadequate advice', 'Incorrect/inadequate advice'), ('Incorrect/inadequate cost disclosure', 'Incorrect/inadequate cost disclosure'), ('Incorrect/inadequate product information', 'Incorrect/inadequate product information'), ('Incorrect/process disclosure', 'Incorrect/process disclosure'), ('Lack of staff training', 'Lack of staff training'), ('Loan Hardship/Postponement', 'Loan Hardship/Postponement'), ('Manual processing error', 'Manual processing error'), ('Misunderstanding of legislation', 'Misunderstanding of legislation'), ('Outsourced Activity', 'Outsourced Activity'), ('Paywave - stolen card or dispute', 'Paywave - stolen card or dispute'), ('Policies not followed', 'Policies not followed'), ('Software controls', 'Software controls'), ('Not Applicable', 'Not Applicable')], max_length=200),
        ),
        migrations.AlterField(
            model_name='incident',
            name='root_cause',
            field=models.CharField(choices=[('ATM Error', 'ATM Error'), ('Broker difficult to contact', 'Broker difficult to contact'), ('Core Banking System Error', 'Core Banking System Error'), ('Cyber Fraud', 'Cyber Fraud'), ('Delays due to broker', 'Delays due to broker'), ('Delays due to lender', 'Delays due to lender'), ('Disclosure docs not issued', 'Disclosure docs not issued'), ('Financial Fraud - Vigil', 'Financial Fraud - Vigil'), ('Fraud by Customer', 'Fraud by Customer'), ('Fraud by staff', 'Fraud by staff'), ('Fraud by representative', 'Fraud by representative'), ('Hardware Issue', 'Hardware Issue'), ('Inadequate project governance', 'Inadequate project governance'), ('Incorrect assessment', 'Incorrect assessment'), ('Incorrect/inadequate advice', 'Incorrect/inadequate advice'), ('Incorrect/inadequate cost disclosure', 'Incorrect/inadequate cost disclosure'), ('Incorrect/inadequate product information', 'Incorrect/inadequate product information'), ('Incorrect/process disclosure', 'Incorrect/process disclosure'), ('Lack of staff training', 'Lack of staff training'), ('Loan Hardship/Postponement', 'Loan Hardship/Postponement'), ('Manual processing error', 'Manual processing error'), ('Misunderstanding of legislation', 'Misunderstanding of legislation'), ('Outsourced Activity', 'Outsourced Activity'), ('Paywave - stolen card or dispute', 'Paywave - stolen card or dispute'), ('Policies not followed', 'Policies not followed'), ('Software controls', 'Software controls'), ('Not Applicable', 'Not Applicable')], max_length=200),
        ),
    ]