# Generated by Django 2.2.1 on 2019-05-28 06:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_auto_20190528_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fraud',
            name='action_result',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='result_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='result_hour',
            field=models.IntegerField(blank=True, help_text='0 to 24', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='result_minute',
            field=models.IntegerField(blank=True, help_text='0 to 60', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='incident',
            name='risk_category_2',
            field=models.CharField(choices=[('Assessment and Quality of Porfolio and Sector', 'Assessment and Quality of Porfolio and Sector'), ('Credit risk appetite', 'Credit risk appetite'), ('Lending security and bad debt management process', 'Lending security and bad debt management process'), ('Product characteristics', 'Product characteristics'), ('Public Safety', 'Public Safety'), ('Socio Economic', 'Socio Economic'), ('Market Risk Appetite', 'Market Risk Appetite'), ('Portfolio Characteristics', 'Portfolio Characteristics'), ('Product/market Characteristics', 'Product/market Characteristics'), ('Trading Limits', 'Trading Limits'), ('Disasters & Utilities Failures', 'Disasters & Utilities Failures'), ('Outsourcing/supplier risk', 'Outsourcing/supplier risk'), ('Political & Economic', 'Political & Economic'), ('Unethical / Criminal Activities', 'Unethical / Criminal Activities'), ('Dysfunctional Behaviour', 'Dysfunctional Behaviour'), ('Employee Fraud', 'Employee Fraud'), ('Inadequate Resources', 'Inadequate Resources'), ('Information Security Abuse', 'Information Security Abuse'), ('People Management', 'People Management'), ('Training and Competence', 'Training and Competence'), ('Unauthorised Activity', 'Unauthorised Activity'), ('Account Opening / Servicing', 'Account Opening / Servicing'), ('Client customer proposition', 'Client customer proposition'), ('Corporate Governance', 'Corporate Governance'), ('Financials', 'Financials'), ('Insurance', 'Insurance'), ('Payment / Settlement / Delivery / Reconciliation Risk', 'Payment / Settlement / Delivery / Reconciliation Risk'), ('Process Design, Product Development and Launch', 'Process Design, Product Development and Launch'), ('Process Management', 'Process Management'), ('Project management ', 'Project management '), ('Record Keeping', 'Record Keeping'), ('Reporting & Management Information', 'Reporting & Management Information'), ('Risk and Compliance', 'Risk and Compliance'), ('Valuation / Pricing', 'Valuation / Pricing'), ('Employment law', 'Employment law'), ('Financial Reporting', 'Financial Reporting'), ('Legal / Public Liability', 'Legal / Public Liability'), ('Regulatory Requirements', 'Regulatory Requirements'), ('Electrical', 'Electrical'), ('Hazardous Substances', 'Hazardous Substances'), ('Mechanical', 'Mechanical'), ('Personal', 'Personal'), ('Plants and Animals', 'Plants and Animals'), ('Radiation', 'Radiation'), ('Site', 'Site'), ('Adequacy of Capital', 'Adequacy of Capital'), ('Brand Management', 'Brand Management'), ('Competition', 'Competition'), ('Economic Environment', 'Economic Environment'), ('Product Proposition', 'Product Proposition'), ('Strategic Planning', 'Strategic Planning'), ('Strategic Risk', 'Strategic Risk'), ('Development and implementation', 'Development and implementation'), ('Existing Systems Management', 'Existing Systems Management'), ('System Outrage and Disruption', 'System Outrage and Disruption'), ('System Security Breach', 'System Security Breach')], max_length=100),
        ),
        migrations.AlterField(
            model_name='incident',
            name='risk_category_3',
            field=models.CharField(blank=True, choices=[('Inadequate management of risks presented by connected exposures.', 'Inadequate management of risks presented by connected exposures.'), ('Inadequate process for identifying trends in volume, sector and concentrations.', 'Inadequate process for identifying trends in volume, sector and concentrations.'), ('Failure to indentify trends in portfolio quality and respond appropriately.', 'Failure to indentify trends in portfolio quality and respond appropriately.'), ('Failure to prepare and follow rationales for responsible lending which are in accordance with approved credit risk policy.', 'Failure to prepare and follow rationales for responsible lending which are in accordance with approved credit risk policy.'), ('Sanctioning authorities monitored', 'Sanctioning authorities monitored'), ('Other', 'Other'), ('Inappropriate credit risk appetitie', 'Inappropriate credit risk appetitie'), ('Inadequate procedures for escalating required changes to credit risk policy', 'Inadequate procedures for escalating required changes to credit risk policy'), ('Scorecard performance and cutt-off', 'Scorecard performance and cutt-off'), ('Failure to manage concentrations of credit risk', 'Failure to manage concentrations of credit risk'), ('Other', 'Other'), ('Failure to make provision for recovery of debt / bad debt.', 'Failure to make provision for recovery of debt / bad debt.'), ('Inappropriate use of credit derivatives to offset investment', 'Inappropriate use of credit derivatives to offset investment'), ('Guarantees', 'Guarantees'), ('Approved credit policy not implemented and monitored.', 'Approved credit policy not implemented and monitored.'), ('Other', 'Other'), ('Failure to appropriately balance off balance sheet counterparty exposures with derivatives, contigent exposures and underwriting', 'Failure to appropriately balance off balance sheet counterparty exposures with derivatives, contigent exposures and underwriting'), ('Failure to ensure that settlement, clearing and intra-day exposures meet with the criteria in the approved Credit Risk policy', 'Failure to ensure that settlement, clearing and intra-day exposures meet with the criteria in the approved Credit Risk policy'), ('Failre to use approved / recognised clearing houses and clearing systems', 'Failre to use approved / recognised clearing houses and clearing systems'), ('Inappropriate application of underwriting processes', 'Inappropriate application of underwriting processes'), ('Failure to ensure correct modelling is used', 'Failure to ensure correct modelling is used'), ('Other', 'Other'), ('Air quality', 'Air quality'), ('Unauthorised entry', 'Unauthorised entry'), ('Other', 'Other'), ('Damage to state economy', 'Damage to state economy'), ('Damage to national economy', 'Damage to national economy'), ('Other', 'Other'), ('Other', 'Other'), ('Inappropriate portfolio composition', 'Inappropriate portfolio composition'), ('Interation with other risks, particularly credit risk', 'Interation with other risks, particularly credit risk'), ('Failure to identify trends in portfolio concentrations and respond apropriately', 'Failure to identify trends in portfolio concentrations and respond apropriately'), ('Inappropriate procedures for managing margins', 'Inappropriate procedures for managing margins'), ('Failure to identify trends in positions taken and respond appropriately', 'Failure to identify trends in positions taken and respond appropriately'), ('Other', 'Other'), ('Failure to ensure an approprate balance between OTC and exchange trading', 'Failure to ensure an approprate balance between OTC and exchange trading'), ('Inappropriate mix of investment types/vehicles', 'Inappropriate mix of investment types/vehicles'), ('Failure to provide for risk presented by foreign exchange rates/market convention/insurance exposure.', 'Failure to provide for risk presented by foreign exchange rates/market convention/insurance exposure.'), ('Other', 'Other'), ('Other', 'Other'), ('Physical damage to property including fire and flood', 'Physical damage to property including fire and flood'), ('Unavailability of building eg. Other natural disasters', 'Unavailability of building eg. Other natural disasters'), ('Utilities failure', 'Utilities failure'), ('Inappropriate BCP planning & Testing', 'Inappropriate BCP planning & Testing'), ('Other', 'Other'), ('Civil unrest', 'Civil unrest'), ('Inappropriate contract/agreement with supplier/outsourcer', 'Inappropriate contract/agreement with supplier/outsourcer'), ('Inappropriate management of client relationships', 'Inappropriate management of client relationships'), ('Breach of contract/service level agreement', 'Breach of contract/service level agreement'), ('Other', 'Other'), ('Change to tax regime', 'Change to tax regime'), ('Change / instability of political regime', 'Change / instability of political regime'), ('Financial Crisis', 'Financial Crisis'), ('Other', 'Other'), ('Third party Fraud', 'Third party Fraud'), ('Terrorism / bomb', 'Terrorism / bomb'), ('External theft / extortion / embezzlement / robbery', 'External theft / extortion / embezzlement / robbery'), ('Theft of intellectual property incorporating programming fraud & misuse of URLs external source', 'Theft of intellectual property incorporating programming fraud & misuse of URLs external source'), ('Market Abuse / Manipulation', 'Market Abuse / Manipulation'), ('Hostage taking / Kidnapping', 'Hostage taking / Kidnapping'), ('Other', 'Other'), ('Churning and switching', 'Churning and switching'), ('Deliberate sabatage to company reputation', 'Deliberate sabatage to company reputation'), ('Deliberate non-compliance with approved policies and/or ignoring /short-circuiting procedures.', 'Deliberate non-compliance with approved policies and/or ignoring /short-circuiting procedures.'), ('Other', 'Other'), ('Misappropriation of phyisical assets', 'Misappropriation of phyisical assets'), ('Maliciaous destruction of physical assets', 'Maliciaous destruction of physical assets'), ('Collusion', 'Collusion'), ('Theft of intellectual property', 'Theft of intellectual property'), ('Bribes / kickbacks', 'Bribes / kickbacks'), ('Other', 'Other'), ('Loss of key personnel', 'Loss of key personnel'), ('Other', 'Other'), ('System / service abuse', 'System / service abuse'), ('Misuse of information assts', 'Misuse of information assts'), ('Other', 'Other'), ('Industrial Action', 'Industrial Action'), ('Ineffective management of people through change', 'Ineffective management of people through change'), ('Human error (unintentional)', 'Human error (unintentional)'), ('Internal communication failure', 'Internal communication failure'), ('Inappropriate remuneration policy and practice', 'Inappropriate remuneration policy and practice'), ('Other', 'Other'), ('Training / Competence', 'Training / Competence'), ('Supervision', 'Supervision'), ('Other', 'Other'), ('Intential unauthorised transaction type/amount', 'Intential unauthorised transaction type/amount'), ('Intentional Mismarking of position', 'Intentional Mismarking of position'), ('Market manipulation / Abuse', 'Market manipulation / Abuse'), ('Activity in unauthorised product', 'Activity in unauthorised product'), ('Limit breach (deliberate)', 'Limit breach (deliberate)'), ('Activity outside authorised counterparty / customer, jurisdictions, mandates, currencies and exchange rules', 'Activity outside authorised counterparty / customer, jurisdictions, mandates, currencies and exchange rules'), ('Other', 'Other'), ('Inaccurate customer / client communication and literature', 'Inaccurate customer / client communication and literature'), ('Failure to ensure completeness of customer/client documentation', 'Failure to ensure completeness of customer/client documentation'), ('Data entry or maintenance error', 'Data entry or maintenance error'), ('Failure to manage clients/customer relationships.', 'Failure to manage clients/customer relationships.'), ('Other', 'Other'), ('Failure to effectively utilise distribution channels', 'Failure to effectively utilise distribution channels'), ('Other', 'Other'), ('Inappropriate risk assessment and monitoring', 'Inappropriate risk assessment and monitoring'), ('Inappropriate loss reporting and validation', 'Inappropriate loss reporting and validation'), ('Other', 'Other'), ('Inadequate asset management', 'Inadequate asset management'), ('Ineffective budgetary and financial process', 'Ineffective budgetary and financial process'), ('Inappropriate liquidity management framework', 'Inappropriate liquidity management framework'), ('Inappropriate projections of liquidity performance', 'Inappropriate projections of liquidity performance'), ('Inadequate financial planning', 'Inadequate financial planning'), ('Other', 'Other'), ('Other', 'Other'), ('Reconciliation process failure', 'Reconciliation process failure'), ('Other', 'Other'), ('Non compliance with authorisation / approval process', 'Non compliance with authorisation / approval process'), ('Failure to identify new process/product in adequacies', 'Failure to identify new process/product in adequacies'), ('Failure to effectively manage product/process launch', 'Failure to effectively manage product/process launch'), ('Other', 'Other'), ('Information risk', 'Information risk'), ('Other / general process management or design', 'Other / general process management or design'), ('Ineffective management of projects', 'Ineffective management of projects'), ('Non compliance with PMMS', 'Non compliance with PMMS'), ('Inadequate / inappropriate change management', 'Inadequate / inappropriate change management'), ('Other', 'Other'), ('Failure to utilise MI effectivively', 'Failure to utilise MI effectivively'), ('MI - distribution and relevance', 'MI - distribution and relevance'), ('Inadequate monitoring of product performance', 'Inadequate monitoring of product performance'), ('Other', 'Other'), ('Other', 'Other'), ('Failure to ensure calculations of interest/charges are correct', 'Failure to ensure calculations of interest/charges are correct'), ('Other', 'Other'), ('Failure to adhere to employment law', 'Failure to adhere to employment law'), ('Other', 'Other'), ('Inadequate tax calculation', 'Inadequate tax calculation'), ('Misleading financial reports', 'Misleading financial reports'), ('Other', 'Other'), ('Breach of fiduciary duty / agency duty', 'Breach of fiduciary duty / agency duty'), ('Inappropriate interpretation / drafting of contracts', 'Inappropriate interpretation / drafting of contracts'), ('Non-adherence to Health and Saftey regulations', 'Non-adherence to Health and Saftey regulations'), ('Breach of environmental management', 'Breach of environmental management'), ('Other', 'Other'), ('Non-adherence to AML/CTF regulation', 'Non-adherence to AML/CTF regulation'), ('Non-adherence to ACL regulation', 'Non-adherence to ACL regulation'), ('Non-adherence to AFSL regulation', 'Non-adherence to AFSL regulation'), ('Non-adherence to privacy regulation', 'Non-adherence to privacy regulation'), ('Failure to adhere to codes of practice', 'Failure to adhere to codes of practice'), ('Failure to employ effective/appropriate compliance procedures/monitoring', 'Failure to employ effective/appropriate compliance procedures/monitoring'), ('Ineffective management of compliance findings', 'Ineffective management of compliance findings'), ('Inedquate regulatory reporting', 'Inedquate regulatory reporting'), ('Inappropriate complaint handling', 'Inappropriate complaint handling'), ('Other', 'Other'), ('240v electrical equipment', '240v electrical equipment'), ('Other', 'Other'), ('Carcinogens, geno toxins', 'Carcinogens, geno toxins'), ('Corresive agents', 'Corresive agents'), ('Toxic harmful substances', 'Toxic harmful substances'), ('Solvents', 'Solvents'), ('Fumes', 'Fumes'), ('Flamable Substances', 'Flamable Substances'), ('Explosion', 'Explosion'), ('Biological', 'Biological'), ('Other', 'Other'), ('Aircraft', 'Aircraft'), ('Plant and Equipment', 'Plant and Equipment'), ('Vibration', 'Vibration'), ('Pressure systems', 'Pressure systems'), ('Tools', 'Tools'), ('Other', 'Other'), ('Heat stress', 'Heat stress'), ('Cold stress', 'Cold stress'), ('Manual handling and lifting', 'Manual handling and lifting'), ('Slips and trips', 'Slips and trips'), ('Mental stress', 'Mental stress'), ('Personal security and safety', 'Personal security and safety'), ('Allergies', 'Allergies'), ('Noise', 'Noise'), ('Infectuous Diseases', 'Infectuous Diseases'), ('Ergonomical (eg. chair, desk set up)', 'Ergonomical (eg. chair, desk set up)'), ('Compurer screens', 'Compurer screens'), ('Other', 'Other'), ('Marine animals', 'Marine animals'), ('Land animals', 'Land animals'), ('Stock', 'Stock'), ('Spiders & insects', 'Spiders & insects'), ('Bats', 'Bats'), ('Plant contact', 'Plant contact'), ('Snakes', 'Snakes'), ('Other', 'Other'), ('Radio frequency', 'Radio frequency'), ('Laser', 'Laser'), ('Other', 'Other'), ('Underground', 'Underground'), ('Working at heights', 'Working at heights'), ('In or under water', 'In or under water'), ('Confined Spaces', 'Confined Spaces'), ('Falling object', 'Falling object'), ('Other', 'Other'), ('Composition and quality', 'Composition and quality'), ('Capital adequacy', 'Capital adequacy'), ('Reserve adequacy', 'Reserve adequacy'), ('Access to Capital', 'Access to Capital'), ('Other', 'Other'), ('Failure to manage loss of market share', 'Failure to manage loss of market share'), ('Failure to respond to consolidation of business providers', 'Failure to respond to consolidation of business providers'), ('Other', 'Other'), ('Other', 'Other'), ('Failure to deliver market reponsive products', 'Failure to deliver market reponsive products'), ('Failure to ensure pricing remains competitive', 'Failure to ensure pricing remains competitive'), ('Other', 'Other'), ('Failure to research and plan', 'Failure to research and plan'), ('Failure to respond to new business delivery systems/new technology', 'Failure to respond to new business delivery systems/new technology'), ('Failure to manage product/marketing interdencies within the group', 'Failure to manage product/marketing interdencies within the group'), ('Other', 'Other'), ('Failure to consider implications of strategy', 'Failure to consider implications of strategy'), ('Inappropriate customers targeted', 'Inappropriate customers targeted'), ('Inappropriate markets targeted', 'Inappropriate markets targeted'), ('Inappropriate Products/services targeted in strategy', 'Inappropriate Products/services targeted in strategy'), ('Failure to Manage financial interdependancies across the group', 'Failure to Manage financial interdependancies across the group'), ('Failure of due dilligence on merger and acquisitions', 'Failure of due dilligence on merger and acquisitions'), ('Incompatibility with existing systems', 'Incompatibility with existing systems'), ('Failure to integrate and or migrate with/from exisiting systems', 'Failure to integrate and or migrate with/from exisiting systems'), ('Programming errors (internal / external)', 'Programming errors (internal / external)'), ('Failure of System to meet business requirements', 'Failure of System to meet business requirements'), ('Other', 'Other'), ('Hardware becomes obsolete', 'Hardware becomes obsolete'), ('Lack of Adequate capactiy planning', 'Lack of Adequate capactiy planning'), ('Operational errors', 'Operational errors'), ('Inappropriate/ineffective Data Management', 'Inappropriate/ineffective Data Management'), ('Other', 'Other'), ('Interface failures', 'Interface failures'), ('Software failure', 'Software failure'), ('Failure of internal Telecommunications', 'Failure of internal Telecommunications'), ('Other', 'Other'), ('Computer viruses', 'Computer viruses'), ('Logical access security breaches', 'Logical access security breaches'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]