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
Password.send_keys('animeshsingh.123')
LogIn = driver.find_element_by_xpath('//*[@type = "submit"]')
LogIn.click()
driver.get('https://www.linkedin.com/in/amrish-rau-4158339/?originalSubdomain=in')
sel = Selector(text = driver.page_source)
li_classes = sel.xpath('//*[@class = "pv-browsemap-section__member-container mt4"]')
time.sleep(3)

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

# YaaaY!!! we got the names...!

# Let's get the Description boys..!!!...

desc = []
for data in indiv_cont.xpath('div/p/text()').extract():
    desc.append(data)

#Yooooooooooooo...>..!!! We got the description toooo!!! Damn Son!!!

# Writing this bitch to csv

writer = csv.writer(open('data_incep_2.csv','w'))
writer.writerow(['Name','Description','LinkedIn Account'])


# Getting One step further into the inception
for i in range(10):
    driver.get(final_links[i])
    sel = Selector(text = driver.page_source)
    indiv_cont = sel.xpath('//a[@data-control-name = "browsemap_profile"]')
    LIlinks = []
    for links in indiv_cont.xpath('attribute::href').extract():
        LIlinks.append(links) 
    for links in LIlinks:
        links = ('https://www.linkedin.com' + links)
        final_links.append(links)
    
    
    for data in indiv_cont.xpath('div/p/text()').extract():
        desc.append(data)


    for names in indiv_cont.xpath('child::*/attribute::alt').extract():
        Name.append(names)

with open('data_incep_3.csv','w',encoding = "utf-8") as myfile:
    writer = csv.writer(myfile)
    writer.writerow(['Name','Description','LinkedIn Account'])
    for i in range(len(Name)):
        writer.writerow([Name[i],desc[i],final_links[i]])
myfile.close()
    
    
    
