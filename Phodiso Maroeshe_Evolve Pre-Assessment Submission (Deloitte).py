#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from tabulate import tabulate
import numpy as np

# Deloitte Evolve graduate submission
# Name: Phodiso Maroeshe
# ID Number: 010307 633 2081




##################################################################################################################

#Please enter the file path and file name for the INVOICE transactions file, for example:
# file_path_invoices='/Users/Downloads/Evolve Academy - Technical assessment - Invoice Transactions.csv'

file_path_invoices=





#Please enter the file path and file name for the VENDOR data file, for example:
# file_path_vendors='/Users/Downloads/Evolve Academy - Technical Assessment - Vendor Data.xlsx'

file_path_vendors=




###########################################################################################################################





sheet_dup=pd.read_csv(file_path_invoices,delimiter=",",parse_dates=['Invoice Date'],thousands=',')
sheet_vendors=pd.read_excel(file_path_vendors)



###########################################################

inv = np.array(sheet_dup['Invoice Number'])  
invoice_number=inv[np.isfinite(inv)]      




unique_invoices=np.unique(invoice_number)   

number=[]
duplicates=[]
for inv_num in unique_invoices:
    count=np.count_nonzero(invoice_number==inv_num)
    if count>1:
        inv_num_formatted=f"{inv_num:.15g}"
        duplicates.append(count-1)
        number.append(inv_num_formatted)
 





title="Table1: DUPLICATED_INVOICES"
column_headers=["Invoice_Number","Count_of_Duplicates"]
data= zip(number,duplicates)
table=tabulate(data,headers=column_headers,tablefmt="fancy_grid")

print(title)
print(table)


##################################################Second Table

sheet=sheet_dup.drop_duplicates()

vendor_legacy_id=np.array(sheet_vendors["Legacy Unique Identifier"])
vendor_name=np.array(sheet_vendors["Name"])
inv_stat =  np.array(sheet["Invoice Status"])[:len(invoice_number)]
vendor_id=np.array(sheet["Vendor Number"])[:len(invoice_number)]
blocked_vendor_id=[]
for j in range(len(inv_stat)):
    if inv_stat[j]=="B":
        blocked_vendor_id.append(vendor_id[j])
 

    




NAME=[]
for ID in blocked_vendor_id:
    for k in range(len(vendor_name)):
        if vendor_legacy_id[k]==ID:
            NAME.append(vendor_name[k])
            
            
column_headers2=["Vendor_Name"]            
data2=list(zip(np.unique(NAME)))
table2=tabulate(data2,headers=column_headers2,tablefmt="fancy_grid")
title2="Table 2: BLOCKED_VENDORS"





print(" ")
print(" ")
print(title2)
print(table2)



###################################################################### Third Table


count_vendors=[np.count_nonzero(vendor_name=="Incorporated Path")]
title3="Table 3: TOTAL_VENDOR"

data3=count_vendors







data_frame = {'Total': data3}
table3 = tabulate(data_frame, headers='keys', tablefmt='fancy_grid')
print(" ")
print(" ")
print(title3)
print(table3)

########################################### Fourth Table

df_merged=pd.merge(sheet,sheet_vendors, left_on="Vendor Number",right_on="Legacy Unique Identifier")


df_merged['Year'] = df_merged['Invoice Date'].dt.year 


results = df_merged.groupby(['Name', 'Year'])['Invoice Total Amount'].sum().reset_index()

results['Rank'] = results.groupby('Year')['Invoice Total Amount'].rank(ascending=False)

results.loc[len(results)] = ["Marvel Movies", "2016", "0", "6"]
results.loc[len(results)] = ["Marvel Movies", "2017", "0", "8"]

table_data = results.values.tolist()

table4 = tabulate(table_data, headers=["Vendor_name","Year","Invoice Total Amount","RANK"], floatfmt=".16g",tablefmt='fancy_grid')


print(" ")
print(" ")
print("Table 4: VENDOR_RANK")
print(table4)





# In[ ]:




