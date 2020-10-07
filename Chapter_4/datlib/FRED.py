#FRED>py
import pandas as pd
import pandas_datareader.data as web
import datetime

def gather_data(data_codes, start, 
                end = datetime.datetime.today(), freq="A"):
#2d would be every 2 days, 3m is 3 months, a quarter, we used A annual
    #check if new column is first column of data
    #if true then create a new dataframe
    i = 0
    for key, code in data_codes.items():
        if i == 0:
            df = web.DataReader(code, "fred", start, end).resample(freq).mean()
            #rename column so that code is replaced by the key (variable name)
            df.rename(columns = {code:key}, inplace = True)
            i = None
        else:
            #if DataFrame exists, add new column
            df[key] = web.DataReader(code, "fred", start, end).resample(freq).mean()
    return df
    #if not, add to existing dataframe
    
def bil_to_mil(series):
#mult billion by 1000 to yield millions
    return series * 10 ** 3

"""
Created on Tue Sep 29 10:54:59 2020

@author: gwens
"""

