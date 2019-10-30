from bs4 import BeautifulSoup 
from selenium import webdriver
from parsel import Selector
import csv

import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.mouthshut.com/')
time.sleep(3) #change it according to the need
search_bar = driver.find_element_by_id('searchProd')

search_bar.send_keys('Honda Activa 5G')  # THIS CAN BE CHANGED TO ANYTHING/ANY PRODUCT YOU WISH TO SEARCH ON

search_but = driver.find_element_by_class_name('hmsrch')
search_but.click()
Ist_res = driver.find_element_by_id('productRepeater_ctl00_hypProduct')
Ist_res.click()
emailid = driver.find_element_by_id('loginId')
emailid.send_keys('animeshr18a')
pwd = driver.find_element_by_id('pwd')
pwd.send_keys('killer')
si = driver.find_element_by_id('btnAjax_Login')
si.click()

#first review
#rev1 = driver.find_element_by_id('ct100_ct100_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ct100_lnkTitle')
#do one thing, store links of all reviews and access them one by one.

#so this only extracts reviews present on first page
sel = Selector(text = driver.page_source)
pages_links = sel.xpath('//*[@class = "btn btn-link"]/attribute::href').extract()

for i in range(5): # so this extracts the reviews from next 5 pages
    
    sel = Selector(text = driver.page_source)
    all_rev_links = sel.xpath('//*[@class = "read-review-holder"]/div[@class = "row review-article"]/div/div/strong/a/attribute::href').extract()
    with open('ms_rev_link.csv','a') as myfile:
        writer = csv.writer(myfile)
        writer.writerows([link] for link in all_rev_links)
    myfile.close()
    driver.get(pages_links[i])    
    