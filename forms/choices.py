RISK_OWNER_CHOICES = (
    ('Managing Director - GMY','Managing Director - GMY'),
    ('GM Banking & Wholesale','GM Banking & Wholesale'),
    ('GM Aggregation','GM Aggregation'),
    ('Group CFO','Group CFO'),
    ('Banking CFO / Company Sec','Banking CFO / Company Sec'),
    ('Chief Risk Officer','Chief Risk Officer'),
    ('Head of Technology and Operations','Head of Technology and Operations'),
    ('Managing Director - Finsure','Managing Director - Finsure'),
    ('Board','Board'),

)
RISK_RATING_CHOICES = (
    ('1. LOW','1. Low'),
    ('2. MODERATE', '2. Moderate'),
    ('3. HIGH','3. Hight'),
    ('4. EXTREME', '4. Extreme'),
    ('5. NEW', '5. New')
)
CONSEQUENCE_CHOICES = (
    ('1. Insignificant','1. Insignificant'),
    ('2. Minor','2. Minor'),
    ('3. Moderate','3. Moderate'),
    ('4. Major','4. Major'),
    ('5. Catastrophic','5. Catastrophic'),
)
APPLICATION_CHOICES = (
    ('Banking, Wholesale and Aggregation','Banking, Wholesale and Aggregation'),

    ('Banking only','Banking only'),
    ('Wholesale only','Wholesale only'),
    ('Aggregation only','Aggregation only'),
    ('Banking and Wholesale','Banking and Wholesale'),
    ('Wholesale and Aggregation','Wholesale and Aggregation'),
    ('Banking and Aggregation','Banking and Aggregation'),

)
RISK_OWNER_EMAILS = {
    'Managing Director - GMY':'sellis@goldfieldsmoney.com.au',
    'GM Banking & Wholesale':'allan.savins@finsure.com.au',
    'GM Aggregation':'simon.bednar@finsure.com.au',
    'Group CFO':'jussi.nunes@bnk.com.au',
    'Banking CFO / Company Sec':'mcowell@goldfieldsmoney.com.au',
    'Chief Risk Officer':'sellis@goldfieldsmoney.com.au',
    'Head of Technology and Operations':'dean.rushton@finsure.com.au',
    'Managing Director - Finsure':'sellis@goldfieldsmoney.com.au',
    'Board':'sellis@goldfieldsmoney.com.au',
    'Head of Technology & Operations':'sellis@goldfieldsmoney.com.au',
}
ADI_CHOICES = (
    ('Adelaide Bank','Adelaide Bank'),
    ('Alliance Bank','Alliance Bank'),
    ('AMP Bank Ltd','AMP Bank Ltd'),
    ('Arab Bank Australia Limited','Arab Bank Australia Limited'),
    ('ANZ','ANZ'),
    ('Australian Central Credit Union Ltd (trading as Peoples Choice Credit Union)','Australian Central Credit Union Ltd (trading as Peoples Choice Credit Union)'),
    ('Australian Military Bank Ltd','Australian Military Bank Ltd'),
    ('Australian Settlements Limited (provides industry services)','Australian Settlements Limited (provides industry services)'),
    ('Australian Unity Bank Limited','Australian Unity Bank Limited'),
    ('Auswide Bank Ltd','Auswide Bank Ltd'),
    ('AWA Alliance Bank','AWA Alliance Bank'),
    ('B&E Ltd (trading as Bank of us)','B&E Ltd (trading as Bank of us)'),
    ('Bananacoast Community Credit Union Ltd','Bananacoast Community Credit Union Ltd'),
    ('Bank Australia Limited','Bank Australia Limited'),
    ('Bank of China (Australia) Limited','Bank of China (Australia) Limited'),
    ('Bank of Melbourne','Bank of Melbourne'),
    ('Bank of Queensland Limited','Bank of Queensland Limited'),
    ('Bank of Sydney Ltd','Bank of Sydney Ltd'),
    ('BankSA','BankSA'),
    ('Bankwest','Bankwest'),
    ('BDCU Alliance Bank','BDCU Alliance Bank'),
    ('Bendigo and Adelaide Bank Limited','Bendigo and Adelaide Bank Limited'),
    ('Bendigo Bank','Bendigo Bank'),
    ('BNK Banking Corporation Limited (previously Goldfields Money Limited)','BNK Banking Corporation Limited (previously Goldfields Money Limited)'),
    ('BOQ Specialists (BOQS)','BOQ Specialists (BOQS)'),
    ('Cairns Penny Savings & Loans Limited (provides general banking services)','Cairns Penny Savings & Loans Limited (provides general banking services)'),
    ('Central Murray Credit Union Limited','Central Murray Credit Union Limited'),
    ('Central West Credit Union Limited','Central West Credit Union Limited'),
    ('Circle Alliance Bank','Circle Alliance Bank'),
    ('Citigroup Pty Limited','Citigroup Pty Limited'),
    ('Coastline Credit Union Limited','Coastline Credit Union Limited'),
    ('Commonwealth Bank of Australia','Commonwealth Bank of Australia'),
    ('Community CPS Australia Limited (trading as Beyond Bank Australia)','Community CPS Australia Limited (trading as Beyond Bank Australia)'),
    ('Community First Credit Union Limited','Community First Credit Union Limited'),
    ('Community Sector Banking','Community Sector Banking'),
    ('Credit Union Australia Ltd','Credit Union Australia Ltd'),
    ('Credit Union SA Ltd','Credit Union SA Ltd'),
    ('Cuscal Limited (provides industry services)','Cuscal Limited (provides industry services)'),
    ('Defence Bank Limited','Defence Bank Limited'),
    ('Delphi Bank','Delphi Bank'),
    ('Dnister Ukrainian Credit Co-operative Limited','Dnister Ukrainian Credit Co-operative Limited'),
    ('EECU Limited (trading as Nexus Mutual)','EECU Limited (trading as Nexus Mutual)'),
    ('Endeavour Mutual Bank Ltd','Endeavour Mutual Bank Ltd'),
    ('Family First Credit Union Limited','Family First Credit Union Limited'),
    ('Fire Service Credit Union Limited','Fire Service Credit Union Limited'),
    ('Firefighters & Affiliates Credit Co-operative Limited','Firefighters & Affiliates Credit Co-operative Limited'),
    ('First Choice Credit Union Ltd','First Choice Credit Union Ltd'),
    ('First Option Bank Ltd','First Option Bank Ltd'),
    ('Ford Co-operative Credit Society Limited (trading as Geelong Bank)','Ford Co-operative Credit Society Limited (trading as Geelong Bank)'),
    ('G&C Mutual Bank Limited','G&C Mutual Bank Limited'),
    ('Gateway Bank Ltd','Gateway Bank Ltd'),
    ('Goulburn Murray Credit Union Co-operative Limited','Goulburn Murray Credit Union Co-operative Limited'),
    ('Greater Bank Limited','Greater Bank Limited'),
    ('Heritage Bank Limited','Heritage Bank Limited'),
    ('Holiday Coast Credit Union Ltd','Holiday Coast Credit Union Ltd'),
    ('Horizon Credit Union Ltd','Horizon Credit Union Ltd'),
    ('HSBC Bank Australia Limited','HSBC Bank Australia Limited'),
    ('Hume Bank Limited','Hume Bank Limited'),
    ('Hunter United Employees Credit Union Limited','Hunter United Employees Credit Union Limited'),
    ('Illawarra Credit Union Limited','Illawarra Credit Union Limited'),
    ('IMB Ltd (trading as IMB Bank)','IMB Ltd (trading as IMB Bank)'),
    ('Indue Ltd','Indue Ltd'),
    ('ING Bank (Australia) Limited (trading as ING)','ING Bank (Australia) Limited (trading as ING)'),
    ('Judo Bank Pty Ltd','Judo Bank Pty Ltd'),
    ('Laboratories Credit Union Limited','Laboratories Credit Union Limited'),
    ('Lithuanian Co-operative Credit Society "Talka" Limited','Lithuanian Co-operative Credit Society "Talka" Limited'),
    ('Lutheran Laypeoples League of Australia','Lutheran Laypeoples League of Australia'),
    ('Lysaght Credit Union Ltd','Lysaght Credit Union Ltd'),
    ('MacArthur Credit Union Ltd','MacArthur Credit Union Ltd'),
    ('Macquarie Bank Limited','Macquarie Bank Limited'),
    ('Macquarie Credit Union Limited','Macquarie Credit Union Limited'),
    ('Maitland Mutual Buiding Society Limited','Maitland Mutual Buiding Society Limited'),
    ('MCU Ltd','MCU Ltd'),
    ('Members Banking Group Limited (trading as RACQ Bank)','Members Banking Group Limited (trading as RACQ Bank)'),
    ('Members Equity Bank Limited','Members Equity Bank Limited'),
    ('MyLifeMyFinance Limited','MyLifeMyFinance Limited'),
    ('MyState Bank Limited','MyState Bank Limited'),
    ('National Australia Bank Limited','National Australia Bank Limited'),
    ('Newcastle Permanent Building Society Limited','Newcastle Permanent Building Society Limited'),
    ('Northern Inland Credit Union Limited','Northern Inland Credit Union Limited'),
    ('Orange Credit Union Limited','Orange Credit Union Limited'),
    ('Police & Nurses Limited (trading as P&N Bank)','Police & Nurses Limited (trading as P&N Bank)'),
    ('Police Bank Ltd (trading as Border Bank)','Police Bank Ltd (trading as Border Bank)'),
    ('Police Credit Union Limited','Police Credit Union Limited'),
    ('Police Financial Services Limited (trading as BankVic)','Police Financial Services Limited (trading as BankVic)'),
    ('Pulse Credit Union Limited','Pulse Credit Union Limited'),
    ('QPCU Limited (trading as QBANK)','QPCU Limited (trading as QBANK)'),
    ('Qudos Mutual Ltd (trading as Qudos Bank)','Qudos Mutual Ltd (trading as Qudos Bank)'),
    ('Queensland Country Credit Union Limited','Queensland Country Credit Union Limited'),
    ('Queensland Professional Credit Union Ltd','Queensland Professional Credit Union Ltd'),
    ('Rabobank Australia Limited','Rabobank Australia Limited'),
    ('Railways Credit Union Limited (trading as MOVE)','Railways Credit Union Limited (trading as MOVE)'),
    ('Regional Australia Bank Ltd','Regional Australia Bank Ltd'),
    ('Reliance Bank','Reliance Bank'),
    ('RSL Money','RSL Money'),
    ('Rural Bank Limited (a subsidiary of Bendigo and Adelaide Bank Limited)','Rural Bank Limited (a subsidiary of Bendigo and Adelaide Bank Limited)'),
    ('Service One Alliance Bank','Service One Alliance Bank'),
    ('South West Slopes Credit Union Ltd','South West Slopes Credit Union Ltd'),
    ('Southern Cross Credit Union Ltd','Southern Cross Credit Union Ltd'),
    ('South-West Credit Union Co-Operative Limited','South-West Credit Union Co-Operative Limited'),
    ('St George Bank','St George Bank'),
    ('Summerland Financial Services Limited (trading as Summerland Credit Union)','Summerland Financial Services Limited (trading as Summerland Credit Union)'),
    ('Suncorp-Metway Limited','Suncorp-Metway Limited'),
    ('Sydney Credit Union Ltd','Sydney Credit Union Ltd'),
    ('Teachers Mutual Bank Limited (trading as Firefighters Mutual Bank and UniBank)','Teachers Mutual Bank Limited (trading as Firefighters Mutual Bank and UniBank)'),
    ('The Broken Hill Community Credit Union Ltd','The Broken Hill Community Credit Union Ltd'),
    ('The Capricornian Ltd','The Capricornian Ltd'),
    ('The Gympie Credit Union Ltd','The Gympie Credit Union Ltd'),
    ('The Shire','The Shire'),
    ('Traditional Credit Union Limited','Traditional Credit Union Limited'),
    ('Transport Mutual Credit Union Limited','Transport Mutual Credit Union Limited'),
    ('Tyro Payments Limited','Tyro Payments Limited'),
    ('Ubank','Ubank'),
    ('Unity Bank Limited','Unity Bank Limited'),
    ('Victoria Teachers Limited (trading as Bank First)','Victoria Teachers Limited (trading as Bank First)'),
    ('volt bank Limited','volt bank Limited'),
    ('Warwick Credit Union Ltd','Warwick Credit Union Ltd'),
    ('WAW Credit Union Co-Operative Limited','WAW Credit Union Co-Operative Limited'),
    ('Westpac Banking Corporation','Westpac Banking Corporation'),
    ('Woolworths Employees Credit Union Limited','Woolworths Employees Credit Union Limited'),

)
HINDSIGHT_BOOLEAN_CHOICES=(
        ('', '---------'),
        ("Yes","Yes"),
        ("No","No"),
        ('N/A','Not Applicable')

    )
LOAN_APPROVER_CHOICES = (
('Simon Lyons','Simon Lyons'),
('Allan Savins','Allan Savins'),
('Mark Seaman','Mark Seaman'),
('Nicole Kata','Nicole Kata'),
('Malcolm Cowell','Malcolm Cowell'),
('Gloria Mudge','Gloria Mudge'),
('Philip Morros','Philip Morros'),
('Mark Josephs','Mark Josephs'),
('Tim Mackeen','Tim Mackeen'),
('Jinesh Patel','Jinesh Patel'),
('John Dickinson','John Dickinson'),
('Taylor Cray ','Taylor Cray '),
('Rachel Meakes','Rachel Meakes'),
('Kean Burke','Kean Burke'),
('Paul Hay','Paul Hay'),
('Ben Shirvani','Ben Shirvani'),


)
LOSS_EVENT_CATEGORIES = {
'Internal fraud':{
    'Unauthorised activity':[
        'Transactions not reported (intentional)',
        'Transaction type (unauthorised)',
        'Mismarking of position (intentional)',
    ],
    'Theft and fraud':[
        'Fraud/credit fraud/worthless deposits',
        'Theft/extortion/embezzlement/robbery',
        'Misappropriation of assets',
        'Malicious destruction of assets',
        'Forgery',
        'Cheque kiting',
        'Smuggling',
        'Account take-over/impersonation/ etc',
        'Tax non-compliance/evasion (intentional)',
        'Bribes/kickbacks',
        'Insider trading (not on ADI’s account)',
    ]
},
'External fraud':{
    'Theft and fraud':[
        'Theft/robbery',
        'Forgery',
        'Cheque kiting',
    ],
    'Systems security':[
        'Hacking damage',
        'Theft of information (with monetary loss)',

    ],

},
'Employment practices and workplace safety':{
    'Employee relations':[
        'Compensation/ benefit/ termination issues',
        'Organised labour activity',

    ],
    'Safe environment':[
        'General liability (slip and fall/ etc)',
        'Employee health and safety rules events',
        'Workers’ compensation',

    ],
    'Diversity and discrimination':[
        'All discrimination types',

    ],

},
'Clients/ products and business practices':{
    'Suitability/ disclosure and fiduciary':[
        'Fiduciary breaches/guideline violations',
        'Suitability/disclosure issues (e. g. know your client requirements)',
        'Retail customer disclosure violations',
        'Breach of privacy',
        'Aggressive sales',
        'Account churning',
        'Misuse of confidential information',
        'Lender liability',

    ],
    'Improper business or market practices':[
        'Antitrust',
        'Improper trade/market practices',
        'Market manipulation',
        'Insider trading (on the ADI’s account)',
        'Unlicensed activity',
        'Money laundering',

    ],
    'Product flaws':[
        'Product defects (unauthorised/ etc)',
        'Model errors',

    ],
    'Selection/ sponsorship and exposure':[
        'Failure to investigate client per guidelines',
        'Exceeding client exposure limits',

    ],
    'Advisory activities':[
        'Disputes over performance of advisory activities',

    ],

},
'Damage to physical assets':{
    'Disasters and other events':[
        'Natural disaster losses',
        'Human losses from external sources (e.g.terrorism or vandalism)'

    ]
},
'Business disruption':{
    'Systems':[
        'Hardware',
        'Software',
        'Telecommunications',
        'Utility outage/disruptions',

    ]
},
'Execution/ delivery and process management':{
    'Transaction capture/ execution and maintenance':[
        'Miscommunication',
        'Data entry/ maintenance or loading error',
        'Missed deadline or responsibility',
        'Model/system mis-operation',
        'Accounting error/entity attribution error',
        'Other task mis-performance',
        'Delivery failure',
        'Collateral management failure',
        'Reference data maintenance',

    ],
    'Monitoring and reporting':[
        'Failed mandatory reporting obligation',
        'Inaccurate external report (loss incurred)',

    ],
    'Customer intake and documentation':[
        'Client permissions/disclaimers missing',
        'Legal documents missing/incomplete',

    ],
    'Customer/client account management':[
        'Unapproved access given to accounts',
        'Incorrect client records (loss incurred)',
        'Negligent loss or damage of client assets',

    ],
    'Trade counterparties':[
        'Non-client counterparty mis-performance',
        'Miscellaneous non-client counterparty disputes',

    ],
    'Vendors and suppliers':[
        'Outsourcing',
        'Vendor disputes',

    ],

},

}
RISK_CATEGORIES={
  'Credit': {
    'Assessment & Quality of Portfolio': [
      'Inadequate management of risks presented by connected exposures.',
      'Inadequate process for identifying trends in volume, sector and concentrations.',
      'Failure to indentify trends in portfolio quality and respond appropriately.',
      'Failure to prepare and follow rationales for responsible lending which are in accordance with approved credit risk policy.',
      'Sanctioning authorities monitored',
      'Other'
    ],
    'Credit risk appetite': [
      'Inappropriate credit risk appetitie',
      'Inadequate procedures for escalating required changes to credit risk policy',
      'Scorecard performance and cutt-off',
      'Failure to manage concentrations of credit risk',
      'Other'
    ],
    'Lending security and bad debt management process': [
      'Failure to make provision for recovery of debt / bad debt.',
      'Inappropriate use of credit derivatives to offset investment',
      'Guarantees',
      'Approved credit policy not implemented and monitored.',
      'Other'
    ],
    'Product characteristics': [
      'Failure to appropriately balance off balance sheet counterparty exposures with derivatives, contigent exposures and underwriting',
      'Failure to ensure that settlement, clearing and intra-day exposures meet with the criteria in the approved Credit Risk policy',
      'Failre to use approved / recognised clearing houses and clearing systems',
      'Inappropriate application of underwriting processes',
      'Failure to ensure correct modelling is used',
      'Failure to manage concentrations of credit risk',
      'Other'
    ]
  },
  'Environment': {
    'Public Safety': [
      'Air quality',
      'Unauthorised entry',
      'Other'
    ],
    'Socio Economic': [
      'Damage to state economy',
      'Damage to national economy',
      'Other'
    ]
  },
  'Market': {
    'Market Risk Appetite': [
      'Other'
    ],
    'Portfolio Characteristics': [
      'Inappropriate portfolio composition',
      'Interation with other risks, particularly credit risk',
      'Failure to identify trends in portfolio concentrations and respond apropriately',
      'Inappropriate procedures for managing margins',
      'Failure to identify trends in positions taken and respond appropriately',
      'Other'
    ],
    'Product/market Characteristics': [
      'Failure to ensure an approprate balance between OTC and exchange trading',
      'Inappropriate mix of investment types/vehicles',
      'Failure to provide for risk presented by foreign exchange rates/market convention/insurance exposure.',
      'Other'
    ],
    'Trading Limits': [
      'Other'
    ]
  },
  'Outsourced': {
    'Disasters & Utilities Failures': [
      'Physical damage to property including fire and flood',
      'Unavailability of building eg. Other natural disasters',
      'Utilities failure',
      'Inappropriate BCP planning & Testing',
      'Other',
      'Civil unrest'
    ],

    'Outsourcing/supplier risk': [
        'Inadequate contingency plans in event of supplier/outsourcer incident/failuure/bankruptcy',
      'Inappropriate contract/agreement with supplier/outsourcer',
        'Inappropriate selection of supplier/outsourcer',
      'Inappropriate management of client relationships',
      'Breach of contract/service level agreement',
      'Other'
    ],
    'Political & Economic': [
      'Change to tax regime',
      'Change / instability of political regime',
      'Financial Crisis',
      'Other'
    ],
    'Unethical / Criminal Activities': [
      'Third party Fraud',
      'Terrorism / bomb',
      'External theft / extortion / embezzlement / robbery',
      'Theft of intellectual property incorporating programming fraud & misuse of URLs external source',
      'Market Abuse / Manipulation',
      'Hostage taking / Kidnapping',
      'Other'
    ]
  },
  'People': {
    'Dysfunctional Behaviour': [
      'Churning and switching',
      'Deliberate sabatage to company reputation',
      'Deliberate non-compliance with approved policies and/or ignoring /short-circuiting procedures.',
      'Other'
    ],
    'Employee Fraud': [
      'Misappropriation of phyisical assets',
      'Maliciaous destruction of physical assets',
      'Collusion',
      'Theft of intellectual property',
      'Bribes / kickbacks',
      'Internal Fraud',
      'Other'
    ],
    'Inadequate Resources': [
      'Loss of key personnel',
      'Other'
    ],
    'Information Security Abuse': [
      'System / service abuse',
      'Misuse of information assts',
      'Other'
    ],
    'People Management': [
      'Industrial Action',
      'Ineffective management of people through change',
      'Human error (unintentional)',
      'Internal communication failure',
      'Inappropriate remuneration policy and practice',
      'Other'
    ],
    'Training and Competence': [
      'Training / Competence',
      'Supervision',
      'Other'
    ],
    'Unauthorised Activity': [
      'Intential unauthorised transaction type/amount',
      'Intentional Mismarking of position',
      'Market manipulation / Abuse',
      'Activity in unauthorised product',
      'Limit breach (deliberate)',
      'Activity outside authorised counterparty / customer, jurisdictions, mandates, currencies and exchange rules',
      'Other'
    ]
  },
  'Process': {
    'Account Opening / Servicing': [
      'Inaccurate customer / client communication and literature',
      'Failure to ensure completeness of customer/client documentation',
      'Data entry or maintenance error',
      'Failure to manage clients/customer relationships.',
      'Other'
    ],
    'Client customer proposition': [
      'Failure to effectively utilise distribution channels',
      'Other'
    ],
    'Corporate Governance': [
      'Inappropriate risk assessment and monitoring',
      'Inappropriate loss reporting and validation',
      'Other'
    ],
    'Financials': [
      'Inadequate asset management',
      'Ineffective budgetary and financial process',
      'Inappropriate liquidity management framework',
      'Inappropriate projections of liquidity performance',
      'Inadequate financial planning',
      'Other'
    ],
    'Insurance': [
        'Inadequate Liability Cover',
      'Other'
    ],
    'Payment / Settlement / Delivery / Reconciliation Risk': [
        'Failure of/inadequte payment/settlement/delivery process',
      'Reconciliation process failure',
      'Other'
    ],
    'Process Design, Product Development and Launch': [
      'Non compliance with authorisation / approval process',
      'Failure to identify new process/product in adequacies',
      'Failure to effectively manage product/process launch',
      'Other'
    ],
    'Process Management': [
      'Information risk',
      'Other / general process management or design'
    ],
    'Project management ': [
      'Ineffective management of projects',
      'Non compliance with PMMS',
      'Inadequate / inappropriate change management'
    ],
    'Record keeping': [
      'Other','Loss of records'
    ],
    'Reporting & Management Information': [
      'Failure to utilise MI effectivively',
      'MI - distribution and relevance',
      'Inadequate monitoring of product performance',
      'Other'
    ],
    'Risk and Compliance': [
        'Other'

    ],
    'Valuation / Pricing': [
      'Failure to ensure calculations of interest/charges are correct',
      'Other'
    ]
  },
  'Regulation / Legal': {
    'Employment law': [
      'Failure to adhere to employment law',
      'Other'
    ],
    'Financial Reporting': [
      'Inadequate tax calculation',
      'Misleading financial reports',
      'Other'
    ],
    'Legal / Public Liability': [
      'Breach of fiduciary duty / agency duty',
      'Inappropriate interpretation / drafting of contracts',
      'Non-adherence to Health and Saftey regulations',
      'Breach of environmental management',
      'Other'
    ],
    'Regulatory Requirements': [
    'Breach of legislation',
      'Non-adherence to AML/CTF regulation',
      'Non-adherence to ACL regulation',
      'Non-adherence to AFSL regulation',
      'Non-adherence to privacy regulation',
    'Non-adherence to prudential regulation',
      'Failure to adhere to codes of practice',
      'Failure to employ effective/appropriate compliance procedures/monitoring',
      'Ineffective management of compliance findings',
      'Inedquate regulatory reporting',
      'Inappropriate complaint handling',
      'Other'
    ]
  },
  'Safety': {
    'Electrical': [
      '240v electrical equipment',
      'Other'
    ],
    'Hazardous Substances': [
      'Carcinogens, geno toxins',
      'Corresive agents',
      'Toxic harmful substances',
      'Solvents',
      'Fumes',
      'Flamable Substances',
      'Explosion',
      'Biological',
      'Other'
    ],
    'Mechanical': [
      'Aircraft',
      'Plant and Equipment',
      'Vibration',
      'Pressure systems',
      'Tools',
      'Other'
    ],
    'Personal': [
      'Heat stress',
      'Cold stress',
      'Manual handling and lifting',
      'Slips and trips',
      'Mental stress',
      'Personal security and safety',
      'Allergies',
      'Noise',
      'Infectuous Diseases',
      'Ergonomical (eg. chair, desk set up)',
      'Compurer screens',
      'Other'
    ],
    'Plants and Animals': [
      'Marine animals',
      'Land animals',
      'Stock',
      'Spiders & insects',
      'Bats',
      'Plant contact',
      'Snakes',
      'Other'
    ],
    'Radiation': [
      'Radio frequency',
      'Laser',
      'Other'
    ],
    'Site': [
      'Underground',
      'Working at heights',
      'In or under water',
      'Confined Spaces',
      'Falling object',
      'Other'
    ]
  },
  'Strategy': {
    'Adequacy of Capital': [
      'Composition and quality',
      'Capital adequacy',
      'Reserve adequacy',
      'Access to Capital'
    ],
    'Brand Management': [
    'Failure to manage adverse publicity',
      'Other'
    ],
    'Competition': [
      'Inappropriate response to Competitiion activity (new and exisitng)',
      'Failure to manage loss of market share',
      'Failure to respond to consolidation of business providers',
      'Other'
    ],
    'Economic Environment': [
      'Other'
    ],
    'Product Proposition': [
      'Failure to deliver market reponsive products',
      'Failure to ensure pricing remains competitive',
      'Other'
    ],
    'Strategic Planning': [
      'Failure to deliver business model',
      'Failure to research and plan',
      'Failure to respond to new business delivery systems/new technology',
      'Failure to manage product/marketing interdencies within the group',
      'Other'
    ],
    'Strategic Risk': [
      'Failure to consider implications of strategy',
      'Inappropriate customers targeted',
      'Inappropriate markets targeted',
      'Inappropriate Products/services targeted in strategy',
      'Failure to Manage financial interdependancies across the group',
      'Failure of due dilligence on merger and acquisitions'
    ]
  },
  'System': {
    'Development and implementation': [
      'Incompatibility with existing systems',
      'Failure to integrate and or migrate with/from exisiting systems',
      'Programming errors (internal / external)',
      'Failure of System to meet business requirements',
      'Other'
    ],
    'Existing Systems Management': [
      'Hardware becomes obsolete',
      'Lack of Adequate capactiy planning',
      'Operational errors',
      'Inappropriate/ineffective Data Management',
      'Other'
    ],
    'System Outage and Disruption': [
      'Interface failures',
      'Software failure',
      'Failure of internal Telecommunications',
      'Interdependency risk',
      'Other'
    ],
    'System Security Breach': [
        'External security breaches including hacking',
      'Computer viruses',
      'Logical access security breaches',
      'Other'
    ]
  }
 }
RISK_FACTOR_CHOICES = (
        ('Account Opening / Fulfilment','Account Opening / Fulfilment'),
        ('Breach of any Group ACL conditions - Aggregation','Breach of any Group ACL conditions - Aggregation'),
        ('Breach of any Group ACL conditions - Banking','Breach of any Group ACL conditions - Banking'),
        ('Breach of any Group AFSL conditions','Breach of any Group AFSL conditions'),
        ('Breach of APRA administered legislation or regulation','Breach of APRA administered legislation or regulation'),
        ('Breach of NCCP Act','Breach of NCCP Act'),
        ('Breach of the AML/CTF Act','Breach of the AML/CTF Act'),
        ('Breach of the Privacy Act','Breach of the Privacy Act'),
        ('Breach of the Tax Act','Breach of the Tax Act'),
        ('Capital Adequacy','Capital Adequacy'),
        ('Competition Risk','Competition Risk'),
        ('Complaints including Social Media','Complaints including Social Media'),
        ('Conflict of Interest','Conflict of Interest'),
        ('Contract Risk','Contract Risk'),
        ('Credit concentration risk – portfolio credit concentration / aggregation ','Credit concentration risk – portfolio credit concentration / aggregation '),
        ('Data Risk','Data Risk'),
        ('Denial of Access to Point of Representation (POR) ','Denial of Access to Point of Representation (POR) '),
        ('Financial Reporting Framework','Financial Reporting Framework'),
        ('Fit & Proper','Fit & Proper'),
        ('Fraudulent activity (External)','Fraudulent activity (External)'),
        ('Fraudulent activity (Internal)','Fraudulent activity (Internal)'),
        ('Inappropriate application of Credit Risk Policy','Inappropriate application of Credit Risk Policy'),
        ('Inappropriate Corporate Governance','Inappropriate Corporate Governance'),
        ('Ineffective Risk and Compliance Framework ','Ineffective Risk and Compliance Framework '),
        ('Integration Risk','Integration Risk'),
        ('IT Security Risk','IT Security Risk'),
        ('Key Person Risk','Key Person Risk'),
        ('Liability claim not covered by indemnity insurance','Liability claim not covered by indemnity insurance'),
        ('Loss of IT Communications','Loss of IT Communications'),
        ('Loss of Key Outsourced Dependencies, including Offshoring','Loss of Key Outsourced Dependencies, including Offshoring'),
        ('Loss of Point of Representation (POR)','Loss of Point of Representation (POR)'),
        ('Loss of records','Loss of records'),
        ('Market risk – Interest Rate Risk in the Banking Book (IRRBB)','Market risk – Interest Rate Risk in the Banking Book (IRRBB)'),
        ('Minimum Liquid Holdings Requirement','Minimum Liquid Holdings Requirement'),
        ('Mortgage management risk','Mortgage management risk'),
        ('OSH','OSH'),
        ('Outsourcing Risk – Mortgage Brokers','Outsourcing Risk – Mortgage Brokers'),
        ('Payment Processing Risk','Payment Processing Risk'),
        ('Project Risk','Project Risk'),
        ('Strategic plan risk','Strategic plan risk'),
        ('Theft including cyber extortion','Theft including cyber extortion'),


    )
BU_CHOICES = (
        ("Banking","Banking"),
        ("Wholesale","Wholesale"),
        ("Aggregation","Aggregation")
    )
STATUS_CHOICES = (
    ("Open","Open"),
    ("Closed","Closed"),
 )

"""
g: d, h, j ,k

d: e
h: o
j: f i
k: o

e:
"""

ROOT_CAUSE_CHOICES = (
        ('ATM Error','ATM Error'),
        ('Broker difficult to contact','Broker difficult to contact'),
        ('Core Banking System Error','Core Banking System Error'),
        ('Cyber Fraud','Cyber Fraud'),
        ('Delays due to broker','Delays due to broker'),
        ('Delays due to lender','Delays due to lender'),
        ('Disclosure docs not issued','Disclosure docs not issued'),
        ('Financial Fraud - Vigil','Financial Fraud - Vigil'),
        ('Fraud by Customer','Fraud by Customer'),
        ('Fraud by staff','Fraud by staff'),
        ('Fraud by representative','Fraud by representative'),
        ('Hardware Issue','Hardware Issue'),
        ('Inadequate project governance','Inadequate project governance'),
        ('Incorrect assessment','Incorrect assessment'),
        ('Incorrect/inadequate advice','Incorrect/inadequate advice'),
        ('Incorrect/inadequate cost disclosure','Incorrect/inadequate cost disclosure'),
        ('Incorrect/inadequate product information','Incorrect/inadequate product information'),
        ('Inadequate service/follow-up','Inadequate service/follow-up'),
        ('Incorrect/process disclosure','Incorrect/process disclosure'),
        ('Lack of staff training','Lack of staff training'),
        ('Loan Hardship/Postponement','Loan Hardship/Postponement'),
        ('Manual processing error','Manual processing error'),
        ('Misunderstanding of legislation','Misunderstanding of legislation'),
        ('Outsourced Activity','Outsourced Activity'),
        ('Paywave - stolen card or dispute','Paywave - stolen card or dispute'),
        ('Policies not followed','Policies not followed'),
        ('Software controls','Software controls'),
        ('Not Applicable','Not Applicable'),
    )
BOOLEAN_CHOICES=(
        ("Yes","Yes"),
        ("No","No"),

    )
