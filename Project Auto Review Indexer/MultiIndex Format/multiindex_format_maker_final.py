from selenium import webdriver
from parsel import Selector
import csv
import time
import pandas as pd

path = 'C:\\Users\\Animesh\\ms_activa_rev.csv'
df = pd.read_csv(path)
column_names = ['PROS','CONS']        #column_names should be a list of strings
rows = []
for i in range(len(df)):
    row_dict = df.iloc[i].to_dict()
    split1 = row_dict[column_names[0]].split(',')
    split2 = row_dict[column_names[1]].split(',')
    max_len = max(len(split1),len(split2))
    new_row = row_dict
    
    for j in range(max_len):
        try:
            new_row[column_names[0]] = split1.pop(0)
        except IndexError:
            new_row[column_names[0]] = ''
        try:
            new_row[column_names[1]] = split2.pop(0)
        except IndexError:
            new_row[column_names[1]] = ''
                
        rows.append(new_row)
            
    newdf = pd.DataFrame()