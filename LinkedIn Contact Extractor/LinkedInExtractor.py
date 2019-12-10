# -*- coding: utf-8 -*-
from parsel import Selector
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.linkedin.com')

Signin_button = driver.find_element_by_class_name('nav__button-secondary')
Signin_button.click()
Email = driver.find_element_by_id('username')
Password = driver.find_element_by_id('password')
Email.send_keys('animesh.r18a@gmail.com')
Password.send_keys('************')  #I'm not dumb....lol
LogIn = driver.find_element_by_xpath('//*[@type = "submit"]')
LogIn.click()
driver.get('https://www.linkedin.com/in/dipankar-mukherjee-ab645551/?originalSubdomain=in')
sel = Selector(text = driver.page_source)


# First, we will get links

indiv_cont = sel.xpath('//a[@data-control-name = "browsemap_profile"]')
LIlinks = []
for links in indiv_cont.xpath('attribute::href').extract():
     LIlinks.append(links) 
final_links = []
for links in LIlinks:
    links = ('https://www.linkedin.com' + links)
    final_links.append(links)
    
# Yay!!!! we got the linkssss....

# Let's Get the NAAaaaameEs!!!

Name=[]
for names in indiv_cont.xpath('child::*/attribute::alt').extract():
    Name.append(names)

# Got the names...!

# Let's get the Description ..!!!...

desc = []
for data in indiv_cont.xpath('div/p/text()').extract():
    desc.append(data)




##6th June, adding Designation and Company of the first 10 journalists(for now)


desig = []
comp = []
# Getting One step further into the inception
for i in range(10):
    driver.get(final_links[i])
    time.sleep(2)
    sel = Selector(text = driver.page_source)
    indiv_cont = sel.xpath('//a[@data-control-name = "browsemap_profile"]')
    LIlinks = []
    for links in indiv_cont.xpath('attribute::href').extract():
        LIlinks.append(links) 
    for links in LIlinks:
        links = ('https://www.linkedin.com' + links + str(i))
        final_links.append(links)
    
    
    for data in indiv_cont.xpath('div/p/text()').extract():
        desc.append(data)


    for names in indiv_cont.xpath('child::*/attribute::alt').extract():
        Name.append(names)
    try:
       designation = sel.xpath('//*[@data-control-name = "background_details_company"]/div/h3/text()').extract_first()
       company = sel.xpath('//*[@data-control-name = "background_details_company"]/div/h4/span/text()')[1].extract()           #FOR COLLECTING COMPANY AND DESIGNATION BUT IT
                                                                                                                               #NEEDS TO GO AND LOAD EVERY PAGE :(
    except:
        desig.append('Not-Available')
        comp.append('Not-Available')
    desig.append(designation)
    comp.append(company)
    

with open('data_incep_4.csv','w',encoding = "utf-8") as myfile:
    writer = csv.writer(myfile)
    writer.writerow(['Name','Description','LinkedIn Account','Designation','Company'])
    for i in range(len(Name)):##use len(Name) but then remove designation and company
        try:
            writer.writerow([Name[i],desc[i],final_links[i],desig[i],comp[i]])
        except:

            writer.writerow([Name[i],desc[i],final_links[i]])
myfile.close()
