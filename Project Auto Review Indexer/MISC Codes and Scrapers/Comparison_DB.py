
from bs4 import BeautifulSoup 
import pandas as pd
from selenium import webdriver
from parsel import Selector
import csv
import os

animesh = 'C:\\Users\\Animesh'
path_W3 = os.path.join(animesh,'W3Newspapers_Sources.csv')
path_MW = os.path.join(animesh,'MW_Sources_updated.csv')
w3_base = pd.read_csv(path_W3)
mw_base = pd.read_csv(path_MW)


w3name = w3_base['NAME']
w3name = w3name.str.lower()
w3name = w3name.str.replace('-','')
w3name = w3name.str.replace(' ','')
mwlinks = mw_base['LINKS']
def isnamepresent(name):
    x = mwlinks.str.contains(name,na = False)
    return x.any(axis = 0)
    
arr = []    
    
for i in range(len(w3name)):
    name = w3name.iloc[i]
    arr.append(isnamepresent(name))

arr= pd.DataFrame(arr,columns = ['Contains?'])
arr['Name'] = w3_base['NAME']
arr['Links'] = w3_base['LINK']
