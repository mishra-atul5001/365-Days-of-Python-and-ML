# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:04:29 2021

@author: Atul Mishra
"""

'''
Helping my Freind -- Pawan with some quick codes

Step 1: Loop in Carrier Band Unique values,
Step 2: Subset dataframe on one single value
Step 3: Extract the SEASONAL COMPONENT and save it in an empty dataframe
Step 4: Keeps happening over and over again!
'''

import pandas as pd
import numpy as np

# df_final_1 -> Date,Carrier_Fin,KPI_VALUE
df_final_1 = pd.DataFrame(columns = ['Date','Carrier_Fin','KPI_VALUE'])

unique_vals = df_final_1['Carrier_Fin'].unique().tolist()
# unique_vals = [df_final_1['Carrier_Fin'].unique()]


def fetch_seasonal_component(unique_vals,main_df):
    seasonal_df = pd.DatFrame()
    
    for carrier_band in unique_vals: # 1,2,4,7........
        sub_df = main_df[main_df['Carrier_Fin'] == carrier_band]
        
        # Seasonaliyt transofromation -> Seasonal Components
        
        temp_var = result.seasonal_values()
        sub_df['seasonal_vals'] = temp_var
        
        seasonal_df.concat(sub_df)
        
    return seasonal_df

fetch_seasonal_component(unique_vals,df_final_1)
            
    