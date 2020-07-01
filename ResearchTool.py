from yahoo_fin.stock_info import get_balance_sheet
from yahoo_fin.stock_info import get_income_statement
from yahoo_fin.stock_info import get_cash_flow
import csv
import time

#list of companies for gathering data
list_of_companies = ['snps','stx','swks','tel','txn','v','vrsn','wdc',
'wu','xrx','zbra']

#companies with problems
#dxc
#mchp
#nlok
#ntap
#qrvo
#xlnx


#finished
#'acn','aapl','adbe','adi','adp','ads','adsk',
#'akam','amat','amd','anet','anss','aph','avgo','br','cdns','cdw',
#'crm'
#'fis','ctxs','ctsh','csco',
#'ffiv','fisv','flir',
#'flt','ftnt','glw','gpn','hpe','hpq','ibm','intc','intu','ipgp','it',
#'jkhy','jnpr','keys','klac','ldos','lrcx','ma'
#'msft','msi',
#'mu','mxim','now','nvda','orcl','payc','payx','pypl',
#'qcom',





#setting up the CSV

column_names = ['Current Ratios Period 1','2','3','4',
'Working Capital Period 1','2','3','4',
'Debt to Equity Ratios Period 1','2','3','4',
'Debt to Assets Ratios Period 1','2','3','4',
'Gross Profit Margins Period 1','2','3','4',
'Net Profit Margins Period 1','2','3','4',
'Total Asset Turnover Period 1','2','3',
'Return on Assets Period 1','2','3',
'Inventory Turnover Ratios Period 1','2','3',
'Average Days to Sell Inventory Period 1','2','3',
'Fixed Asset Turnover Ratios Period 1','2','3',
'Accounts Payable Turnover Ratios Period 1','2','3',
'Average Age of Payables Ratios Period 1','2','3',
'Times Interest Earned Ratios Period 1','2','3','4',
'Quality of Income Ratio Period 1','2','3','4']




A = open('InformationTech.csv','w')
writer1 = csv.writer(A)
Col = ['Company'] + column_names
writer1.writerow(Col)


#this for loop cycles through every company
for companies in list_of_companies:
    print(companies)
#add a csv writer that adds these to rows
    data_list = [companies]





    #this is the information from the balance sheet
    Loaded = 0
    company_data = get_balance_sheet(companies)







    
    #no matter how many times I try to redownload the data, the key is always missing





    #this line is being problematic
    Loaded += sum(company_data['Breakdown'].str.count("Total stockholders' equity"))


    while Loaded == 0.0:
            company_data = get_balance_sheet(companies)
            Loaded += sum(company_data['Breakdown'].str.count("Total stockholders' equity"))









    SE1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total stockholders' equity"].index[0],1])
    SE2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total stockholders' equity"].index[0],2])
    SE3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total stockholders' equity"].index[0],3])
    SE4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total stockholders' equity"].index[0],4])

    CA1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Assets"].index[0],1])
    CA2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Assets"].index[0],2])
    CA3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Assets"].index[0],3])
    CA4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Assets"].index[0],4])

    CL1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Liabilities"].index[0],1])
    CL2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Liabilities"].index[0],2])
    CL3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Liabilities"].index[0],3])
    CL4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Current Liabilities"].index[0],4])

    TA1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Assets"].index[0],1])
    TA2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Assets"].index[0],2])
    TA3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Assets"].index[0],3])
    TA4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Assets"].index[0],4])

    TL1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Liabilities"].index[0],1])
    TL2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Liabilities"].index[0],2])
    TL3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Liabilities"].index[0],3])
    TL4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Total Liabilities"].index[0],4])




    check6= 0
    check6 += sum(company_data['Breakdown'].str.count('Accounts Payable'))
    if check6 == 0 or company_data[company_data['Breakdown'].str.match('Accounts Payable')].iloc[0,1] == '-':
        AP1 = 'NULL'
        AP2 = 'NULL'
        AP3 = 'NULL'
        AP4 = 'NULL'
    else:
        AP1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Accounts Payable"].index[0],1])
        AP2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Accounts Payable"].index[0],2])
        AP3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Accounts Payable"].index[0],3])
        AP4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Accounts Payable"].index[0],4])


    check2 = 0
    check2 += sum(company_data['Breakdown'].str.count('Inventory'))
    if check2 == 0 or company_data[company_data['Breakdown'].str.match('Inventory')].iloc[0,2] == '-' or company_data[company_data['Breakdown'].str.match('Inventory')].iloc[0,3] == '-':
        IN1 = 'NULL'
        IN2 = 'NULL'
        IN3 = 'NULL'
        IN4 = 'NULL'
    else:
        IN1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Inventory"].index[0],1])
        IN2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Inventory"].index[0],2])
        IN3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Inventory"].index[0],3])
        IN4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Inventory"].index[0],4])



    PPE1 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Net property plant and equipment"].index[0],1])
    PPE2 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Net property plant and equipment"].index[0],2])
    PPE3 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Net property plant and equipment"].index[0],3])
    PPE4 = float(company_data.iloc[company_data[company_data['Breakdown'] == "Net property plant and equipment"].index[0],4])




    ##################################################
    ##################################################
    ##################################################
















    #this is the information from the income statement
    Loaded = 0
    company_income_data = get_income_statement(companies)





    Loaded += sum(company_income_data['Breakdown'].str.count('Net Income Common Stockholders'))

    while Loaded == 0.0:
        company_income_data = get_income_statement(companies)
        Loaded += sum(company_income_data['Breakdown'].str.count('Net Income Common Stockholders'))


    NI1 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Net Income Common Stockholders'].index[0],2])
    NI2 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Net Income Common Stockholders'].index[0],3])
    NI3 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Net Income Common Stockholders'].index[0],4])
    NI4 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Net Income Common Stockholders'].index[0],5])





    check = 0
    check += sum(company_income_data['Breakdown'].str.count('Interest Expense'))
    if check == 0 or company_income_data[company_income_data['Breakdown'].str.match('Interest Expense')].iloc[0,2] == '-' or company_income_data[company_income_data['Breakdown'].str.match('Interest Expense')].iloc[0,3] == '-' or company_income_data[company_income_data['Breakdown'].str.match('Interest Expense')].iloc[0,5] == '-':
        IE1 = 'NULL'
        IE2 = 'NULL'
        IE3 = 'NULL'
        IE4 = 'NULL'
    else:
        IE1 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Interest Expense'].index[0],2])
        IE2 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Interest Expense'].index[0],3])
        IE3 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Interest Expense'].index[0],4])
        IE4 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Interest Expense'].index[0],5])




    check3 = 0
    check3 +=sum(company_income_data['Breakdown'].str.count('Cost of Revenue'))
    if check3 == 0 or company_income_data[company_income_data['Breakdown'].str.match('Cost of Revenue')].iloc[0,2] == '-':
        COR1 = 'NULL'
        COR2 = 'NULL'
        COR3 = 'NULL'
        COR4 = 'NULL'
    else:
        COR1 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Cost of Revenue'].index[0],2])
        COR2 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Cost of Revenue'].index[0],3])
        COR3 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Cost of Revenue'].index[0],4])
        COR4 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Cost of Revenue'].index[0],5])
    



    TR1 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Total Revenue'].index[0],2])
    TR2 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Total Revenue'].index[0],3])
    TR3 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Total Revenue'].index[0],4])
    TR4 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Total Revenue'].index[0],5])





    check4 = 0
    check4 +=sum(company_income_data['Breakdown'].str.count('Gross Profit'))
    if check4 == 0 or company_income_data[company_income_data['Breakdown'].str.match('Gross Profit')].iloc[0,2] == '-':
        GP1 = 'NULL'
        GP2 = 'NULL'
        GP3 = 'NULL'
        GP4 = 'NULL'
    else:
        GP1 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Gross Profit'].index[0],2])
        GP2 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Gross Profit'].index[0],3])
        GP3 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Gross Profit'].index[0],4])
        GP4 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Gross Profit'].index[0],5])



    check5 = 0
    check5 +=sum(company_income_data['Breakdown'].str.count('Tax Provision'))
    if check5 == 0 or company_income_data[company_income_data['Breakdown'].str.match('Tax Provision')].iloc[0,2] == '-':
        TE1 = 'NULL'
        TE2 = 'NULL'
        TE3 = 'NULL'
        TE4 = 'NULL'
    else:
        TE1 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Tax Provision'].index[0],2])
        TE2 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Tax Provision'].index[0],3])
        TE3 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Tax Provision'].index[0],4])
        TE4 = float(company_income_data.iloc[company_income_data[company_income_data['Breakdown'] == 'Tax Provision'].index[0],5])






    ##################################################
    ##################################################
    ##################################################




    #this is the information from the statement of cash flows
    Loaded = 0
    StatementOfCashFlows = get_cash_flow(companies)


    

    Loaded += sum(StatementOfCashFlows['Breakdown'].str.count('Net cash provided by operating activites'))
    while Loaded == 0.0:
        StatementOfCashFlows = get_cash_flow(companies)
        Loaded += sum(StatementOfCashFlows['Breakdown'].str.count('Net cash provided by operating activites'))



















    WC1 = float(StatementOfCashFlows.iloc[StatementOfCashFlows[StatementOfCashFlows['Breakdown'] == 'Net cash provided by operating activites'].index[0],2])
    WC2 = float(StatementOfCashFlows.iloc[StatementOfCashFlows[StatementOfCashFlows['Breakdown'] == 'Net cash provided by operating activites'].index[0],3])
    WC3 = float(StatementOfCashFlows.iloc[StatementOfCashFlows[StatementOfCashFlows['Breakdown'] == 'Net cash provided by operating activites'].index[0],4])
    WC4 = float(StatementOfCashFlows.iloc[StatementOfCashFlows[StatementOfCashFlows['Breakdown'] == 'Net cash provided by operating activites'].index[0],5])

    #Current Ratios
    CR1 = CA1/CL1
    CR2 = CA2/CL2
    CR3 = CA3/CL3
    CR4 = CA4/CL4
    #working Capital
    WC1 = CA1-CL1
    WC2 = CA2-CL2
    WC3 = CA3-CL3
    WC4 = CA4-CL4
    #debt to equity
    DE1 = TL1/SE1
    DE2 = TL2/SE2
    DE3 = TL3/SE3
    DE4 = TL4/SE4
    #debt to assets
    DA1 = TL1/TA1
    DA2 = TL2/TA2
    DA3 = TL3/TA3
    DA4 = TL4/TA4
    #gross profit margin
    if GP1 == 'NULL':
        GPM1 = 'NULL'
        GPM2 = 'NULL'
        GPM3 = 'NULL'
        GPM4 = 'NULL'
    else:     
        GPM1 = GP1/TR1
        GPM2 = GP2/TR2
        GPM3 = GP3/TR3
        GPM4 = GP4/TR4
    #net profit margin
    NPM1 = NI1/TR1
    NPM2 = NI2/TR2
    NPM3 = NI3/TR3
    NPM4 = NI4/TR4
    #total Asset turnover
    TAT1 = TR1/((TA1+TA2)/2)
    TAT2 = TR2/((TA2+TA3)/2)
    TAT3 = TR3/((TA3+TA4)/2)
    #return on assets
    ROA1 = NPM1*TAT1
    ROA2 = NPM2*TAT2
    ROA3 = NPM3*TAT3
    #inventory turnover
    if IN1 == 'NULL' or COR1 == 'NULL':
        IT1 = 'NULL'
        IT2 = 'NULL'
        IT3 = 'NULL'
    else:
        IT1 = COR1/((IN1+IN2)/2)
        IT2 = COR2/((IN2+IN3)/2)
        IT3 = COR3/((IN3+IN4)/2)
    #average days to sell inventory
    if IN1 == 'NULL' or COR1 == 'NULL':
        ADI1 = 'NULL'
        ADI2 = 'NULL'
        ADI3 = 'NULL'
    else:
        ADI1 = 365/IT1
        ADI2 = 365/IT2
        ADI3 = 365/IT3
    #fixed asset turnover ratio: net sales / PPE
    FAT1 = TR1/((PPE1+PPE2)/2)
    FAT2 = TR2/((PPE2+PPE3)/2)
    FAT3 = TR3/((PPE3+PPE4)/2)
    #accounts payable turnover
    if COR1 == 'NULL' or AP1 == 'NULL':
        APT1 = 'NULL'
        APT2 = 'NULL'
        APT3 = 'NULL'
    else:
        APT1 = COR1/((AP1+AP2)/2)
        APT2 = COR2/((AP2+AP3)/2)
        APT3 = COR3/((AP3+AP4)/2)
    #average age of payables
    if APT1 == 'NULL':
        AAP1 = 'NULL'
        AAP2 = 'NULL'
        AAP3 = 'NULL'
    else:
        AAP1 = 365/APT1
        AAP2 = 365/APT2
        AAP3 = 365/APT3
    #times interest earned ratio: this shows how much larger earnings are to interest 
    #TIER of 3.0 means that earnings available are 3 times larger than interest
    if IE1 == 'NULL' or TE1 == 'NULL':
        TIER1 = 'NULL'
        TIER2 = 'NULL'
        TIER3 = 'NULL'
        TIER4 = 'NULL'
    else:
        TIER1 = (NI1+IE1+TE1)/IE1
        TIER2 = (NI2+IE2+TE2)/IE2
        TIER3 = (NI3+IE3+TE3)/IE3
        TIER4 = (NI4+IE4+TE4)/IE4
    #this is calculating the quality of cash flow(ratio of 1.18 means that cashflow from operations is 1.18 times larger
    # than net income. the higher this ratio, the better)
    QI1 = WC1/NI1
    QI2 = WC2/NI2
    QI3 = WC3/NI3
    QI4 = WC4/NI4



    ListOfRatios = [CR1,CR2,CR3,CR4,WC1,WC2,WC3,WC4,DE1,DE2,DE3,DE4,
    DA1,DA2,DA3,DA4,GPM1,GPM2,GPM3,GPM4,NPM1,NPM2,NPM3,NPM4,TAT1,TAT2,TAT3,ROA1,ROA2,ROA3,
    IT1,IT2,IT3,ADI1,ADI2,ADI3,FAT1,FAT2,FAT3,APT1,APT2,APT3,AAP1,AAP2,AAP3,TIER1,TIER2,TIER3,TIER4,
    QI1,QI2,QI3,QI4]
    #add the ratios from above


    #this is where the csv appends the data list to the row
    writer1.writerow(data_list+ListOfRatios)

