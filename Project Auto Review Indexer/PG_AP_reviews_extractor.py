from selenium import webdriver
from parsel import Selector
import csv

driver = webdriver.Chrome('chromedriver')
driver.get('https://autoportal.com/newbikes/honda/activa/reviews/')  #NOTICE HOW THIS IS ONLY FOR 'HONDA ACTIVA'
sel = Selector(text = driver.page_source)
all_revs = sel.xpath('//*[@id="content"]/div[3]/div[1]/div[2]/div[1]/div[1]/div/h3/a/attribute::href').extract()
pages_links = ['https://autoportal.com/newbikes/honda/activa/reviews/page/' + str(i) for i in range(2,7)] #MAde these manually but these are correct links for the next 5 pages.
for link in pages_links:
    driver.get(link)
    all_revs.extend(sel.xpath('//*[@id="content"]/div[3]/div[1]/div[2]/div[1]/div[1]/div/h3/a/attribute::href').extract())

all_revs_final = ['https://autoportal.com' + link for link in all_revs]
with open('AP_rev_link.csv','a') as myfile:
    writer = csv.writer(myfile)
    writer.writerows([link] for link in all_revs)
myfile.close() 