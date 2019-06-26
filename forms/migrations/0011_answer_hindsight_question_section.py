# Generated by Django 2.2.1 on 2019-05-25 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0010_fraud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='forms.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Hindsight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('funder_policy', models.CharField(choices=[('Adelaide Bank', 'Adelaide Bank'), ('Alliance Bank', 'Alliance Bank'), ('AMP Bank Ltd', 'AMP Bank Ltd'), ('Arab Bank Australia Limited', 'Arab Bank Australia Limited'), ('ANZ', 'ANZ'), ('Australian Central Credit Union Ltd (trading as Peoples Choice Credit Union)', 'Australian Central Credit Union Ltd (trading as Peoples Choice Credit Union)'), ('Australian Military Bank Ltd', 'Australian Military Bank Ltd'), ('Australian Settlements Limited (provides industry services)', 'Australian Settlements Limited (provides industry services)'), ('Australian Unity Bank Limited', 'Australian Unity Bank Limited'), ('Auswide Bank Ltd', 'Auswide Bank Ltd'), ('AWA Alliance Bank', 'AWA Alliance Bank'), ('B&E Ltd (trading as Bank of us)', 'B&E Ltd (trading as Bank of us)'), ('Bananacoast Community Credit Union Ltd', 'Bananacoast Community Credit Union Ltd'), ('Bank Australia Limited', 'Bank Australia Limited'), ('Bank of China (Australia) Limited', 'Bank of China (Australia) Limited'), ('Bank of Melbourne', 'Bank of Melbourne'), ('Bank of Queensland Limited', 'Bank of Queensland Limited'), ('Bank of Sydney Ltd', 'Bank of Sydney Ltd'), ('BankSA', 'BankSA'), ('Bankwest', 'Bankwest'), ('BDCU Alliance Bank', 'BDCU Alliance Bank'), ('Bendigo and Adelaide Bank Limited', 'Bendigo and Adelaide Bank Limited'), ('Bendigo Bank', 'Bendigo Bank'), ('BNK Banking Corporation Limited (previously Goldfields Money Limited)', 'BNK Banking Corporation Limited (previously Goldfields Money Limited)'), ('BOQ Specialists (BOQS)', 'BOQ Specialists (BOQS)'), ('Cairns Penny Savings & Loans Limited (provides general banking services)', 'Cairns Penny Savings & Loans Limited (provides general banking services)'), ('Central Murray Credit Union Limited', 'Central Murray Credit Union Limited'), ('Central West Credit Union Limited', 'Central West Credit Union Limited'), ('Circle Alliance Bank', 'Circle Alliance Bank'), ('Citigroup Pty Limited', 'Citigroup Pty Limited'), ('Coastline Credit Union Limited', 'Coastline Credit Union Limited'), ('Commonwealth Bank of Australia', 'Commonwealth Bank of Australia'), ('Community CPS Australia Limited (trading as Beyond Bank Australia)', 'Community CPS Australia Limited (trading as Beyond Bank Australia)'), ('Community First Credit Union Limited', 'Community First Credit Union Limited'), ('Community Sector Banking', 'Community Sector Banking'), ('Credit Union Australia Ltd', 'Credit Union Australia Ltd'), ('Credit Union SA Ltd', 'Credit Union SA Ltd'), ('Cuscal Limited (provides industry services)', 'Cuscal Limited (provides industry services)'), ('Defence Bank Limited', 'Defence Bank Limited'), ('Delphi Bank', 'Delphi Bank'), ('Dnister Ukrainian Credit Co-operative Limited', 'Dnister Ukrainian Credit Co-operative Limited'), ('EECU Limited (trading as Nexus Mutual)', 'EECU Limited (trading as Nexus Mutual)'), ('Endeavour Mutual Bank Ltd', 'Endeavour Mutual Bank Ltd'), ('Family First Credit Union Limited', 'Family First Credit Union Limited'), ('Fire Service Credit Union Limited', 'Fire Service Credit Union Limited'), ('Firefighters & Affiliates Credit Co-operative Limited', 'Firefighters & Affiliates Credit Co-operative Limited'), ('First Choice Credit Union Ltd', 'First Choice Credit Union Ltd'), ('First Option Bank Ltd', 'First Option Bank Ltd'), ('Ford Co-operative Credit Society Limited (trading as Geelong Bank)', 'Ford Co-operative Credit Society Limited (trading as Geelong Bank)'), ('G&C Mutual Bank Limited', 'G&C Mutual Bank Limited'), ('Gateway Bank Ltd', 'Gateway Bank Ltd'), ('Goulburn Murray Credit Union Co-operative Limited', 'Goulburn Murray Credit Union Co-operative Limited'), ('Greater Bank Limited', 'Greater Bank Limited'), ('Heritage Bank Limited', 'Heritage Bank Limited'), ('Holiday Coast Credit Union Ltd', 'Holiday Coast Credit Union Ltd'), ('Horizon Credit Union Ltd', 'Horizon Credit Union Ltd'), ('HSBC Bank Australia Limited', 'HSBC Bank Australia Limited'), ('Hume Bank Limited', 'Hume Bank Limited'), ('Hunter United Employees Credit Union Limited', 'Hunter United Employees Credit Union Limited'), ('Illawarra Credit Union Limited', 'Illawarra Credit Union Limited'), ('IMB Ltd (trading as IMB Bank)', 'IMB Ltd (trading as IMB Bank)'), ('Indue Ltd', 'Indue Ltd'), ('ING Bank (Australia) Limited (trading as ING)', 'ING Bank (Australia) Limited (trading as ING)'), ('Judo Bank Pty Ltd', 'Judo Bank Pty Ltd'), ('Laboratories Credit Union Limited', 'Laboratories Credit Union Limited'), ('Lithuanian Co-operative Credit Society "Talka" Limited', 'Lithuanian Co-operative Credit Society "Talka" Limited'), ('Lutheran Laypeoples League of Australia', 'Lutheran Laypeoples League of Australia'), ('Lysaght Credit Union Ltd', 'Lysaght Credit Union Ltd'), ('MacArthur Credit Union Ltd', 'MacArthur Credit Union Ltd'), ('Macquarie Bank Limited', 'Macquarie Bank Limited'), ('Macquarie Credit Union Limited', 'Macquarie Credit Union Limited'), ('Maitland Mutual Buiding Society Limited', 'Maitland Mutual Buiding Society Limited'), ('MCU Ltd', 'MCU Ltd'), ('Members Banking Group Limited (trading as RACQ Bank)', 'Members Banking Group Limited (trading as RACQ Bank)'), ('Members Equity Bank Limited', 'Members Equity Bank Limited'), ('MyLifeMyFinance Limited', 'MyLifeMyFinance Limited'), ('MyState Bank Limited', 'MyState Bank Limited'), ('National Australia Bank Limited', 'National Australia Bank Limited'), ('Newcastle Permanent Building Society Limited', 'Newcastle Permanent Building Society Limited'), ('Northern Inland Credit Union Limited', 'Northern Inland Credit Union Limited'), ('Orange Credit Union Limited', 'Orange Credit Union Limited'), ('Police & Nurses Limited (trading as P&N Bank)', 'Police & Nurses Limited (trading as P&N Bank)'), ('Police Bank Ltd (trading as Border Bank)', 'Police Bank Ltd (trading as Border Bank)'), ('Police Credit Union Limited', 'Police Credit Union Limited'), ('Police Financial Services Limited (trading as BankVic)', 'Police Financial Services Limited (trading as BankVic)'), ('Pulse Credit Union Limited', 'Pulse Credit Union Limited'), ('QPCU Limited (trading as QBANK)', 'QPCU Limited (trading as QBANK)'), ('Qudos Mutual Ltd (trading as Qudos Bank)', 'Qudos Mutual Ltd (trading as Qudos Bank)'), ('Queensland Country Credit Union Limited', 'Queensland Country Credit Union Limited'), ('Queensland Professional Credit Union Ltd', 'Queensland Professional Credit Union Ltd'), ('Rabobank Australia Limited', 'Rabobank Australia Limited'), ('Railways Credit Union Limited (trading as MOVE)', 'Railways Credit Union Limited (trading as MOVE)'), ('Regional Australia Bank Ltd', 'Regional Australia Bank Ltd'), ('Reliance Bank', 'Reliance Bank'), ('RSL Money', 'RSL Money'), ('Rural Bank Limited (a subsidiary of Bendigo and Adelaide Bank Limited)', 'Rural Bank Limited (a subsidiary of Bendigo and Adelaide Bank Limited)'), ('Service One Alliance Bank', 'Service One Alliance Bank'), ('South West Slopes Credit Union Ltd', 'South West Slopes Credit Union Ltd'), ('Southern Cross Credit Union Ltd', 'Southern Cross Credit Union Ltd'), ('South-West Credit Union Co-Operative Limited', 'South-West Credit Union Co-Operative Limited'), ('St George Bank', 'St George Bank'), ('Summerland Financial Services Limited (trading as Summerland Credit Union)', 'Summerland Financial Services Limited (trading as Summerland Credit Union)'), ('Suncorp-Metway Limited', 'Suncorp-Metway Limited'), ('Sydney Credit Union Ltd', 'Sydney Credit Union Ltd'), ('Teachers Mutual Bank Limited (trading as Firefighters Mutual Bank and UniBank)', 'Teachers Mutual Bank Limited (trading as Firefighters Mutual Bank and UniBank)'), ('The Broken Hill Community Credit Union Ltd', 'The Broken Hill Community Credit Union Ltd'), ('The Capricornian Ltd', 'The Capricornian Ltd'), ('The Gympie Credit Union Ltd', 'The Gympie Credit Union Ltd'), ('The Shire', 'The Shire'), ('Traditional Credit Union Limited', 'Traditional Credit Union Limited'), ('Transport Mutual Credit Union Limited', 'Transport Mutual Credit Union Limited'), ('Tyro Payments Limited', 'Tyro Payments Limited'), ('Ubank', 'Ubank'), ('Unity Bank Limited', 'Unity Bank Limited'), ('Victoria Teachers Limited (trading as Bank First)', 'Victoria Teachers Limited (trading as Bank First)'), ('volt bank Limited', 'volt bank Limited'), ('Warwick Credit Union Ltd', 'Warwick Credit Union Ltd'), ('WAW Credit Union Co-Operative Limited', 'WAW Credit Union Co-Operative Limited'), ('Westpac Banking Corporation', 'Westpac Banking Corporation'), ('Woolworths Employees Credit Union Limited', 'Woolworths Employees Credit Union Limited')], max_length=200)),
                ('loan_account', models.CharField(max_length=20)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approved_hindsights', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submittedh_hindisights', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_hindsights', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('reviewed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('hindsight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forms.Hindsight')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forms.Question')),
            ],
        ),
    ]
