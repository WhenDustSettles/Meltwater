from bs4 import BeautifulSoup 
import pandas as pd
from selenium import webdriver
from parsel import Selector
import csv
import os
import numpy as np

driver = webdriver.Chrome('chromedriver')

desktop = 'C:\\Users\\Animesh'
path = os.path.join(desktop,'more_IPRD_w_links.csv')
source = pd.read_csv(path)

def URL_Chckr_w_words_extr(name,URL): #name is source['Name'].iloc[i]
    
    words  = name.split()
    
    for i in range(len(words)):
        if (words[i] == 'News') or (words[i] == 'news') or (words[i] == 'The') or (words[i] == 'the') :
            words[i] = ''
    
    name = ' '.join(words)
    name = name.lower()
    words = name.split()
    
    for i in range(len(words)):
        words = np.array(words)
        if((words[i] in URL) and (words[(i+1)%len(words)] in URL)):
            return True
        elif(i == len(words)-1):
            return False
        