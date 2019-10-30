from selenium import webdriver
from parsel import Selector
import csv
import pandas as pd

path = "C:\\Users\\Animesh\\AP_rev_link.csv"
df = pd.read_csv(path)
driver = webdriver.Chrome('chromedriver')
pros = []
cons = []
ratings = []
for i in range(3):
    driver.get(df['LINKS'].iloc[i])
    sel = Selector(text= driver.page_source)
    pros.extend(sel.xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div[1]/ul/li[1]/text()').extract())
    cons.extend(sel.xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div[1]/ul/li[2]/text()').extract())
    ratings.extend(sel.xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div/span/text()').extract())

p = pd.DataFrame(pros)
c = pd.DataFrame(cons)
r = pd.DataFrame(ratings)
df['PROS'] = p
df['CONS'] = c
df['PROS'] = df['PROS'].str.replace('\n',' ')
df['CONS'] = df['CONS'].str.replace('\n',' ')
df['RATING'] = r
df['RATING'] = df['RATING'].str.replace('Overall rating: ','')
####PUT THE NAME OF THE FILE B4 ACTING SMART, THANK YOU.....
df.to_csv('test4.csv')