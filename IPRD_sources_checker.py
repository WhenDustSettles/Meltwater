import time
import pandas as pd
from selenium import webdriver
from parsel import Selector
import numpy as np
import os

driver = webdriver.Chrome('chromedriver')

desktop = 'C:\\Users\\Animesh\\Desktop'
path = os.path.join(desktop,'AP Sources supercleaned.csv')
source = pd.read_csv(path)
driver.get('https://www.google.com/')
input_1 = driver.find_element_by_name("q")  #search bar

input_1.send_keys('site: ' + list(source.iloc[0])[0] + ' .in news')
search_but = driver.find_elements_by_class_name('gNO89b')[1] #search button
search_but.click()
sel = Selector(text = driver.page_source)
first5links = sel.xpath('//*[@class="srg"]/div/div/div/div/a/attribute::href').extract()[:5]    #Extracting the first 5 URLs

###################################DEPRECATED FUNCTION
# To find if something like Times Of India is written as TOI
#def kwrds_extr(name):          #name is source.iloc[i]
#    words = list(name)[0]
#    simplest_name_w_the = words.lower().replace(' ','')
#    words = words.split()
#    for i in range(len(words)):
#        if (words[i] == 'News') or (words[i] == 'news'):
#            words.pop(i)
#            break
#    simplest_name_w_the_wo_news = ''.join(words)
#    if (words[0] == 'The') or (words[0] == 'the'):
#        words.pop(0)
#    simplest_name_wo_the = ''.join(words) 
#    simplest_name_wo_the = simplest_name_wo_the.lower()
#    
#    prefix = [word[0] for word in words]
#    prefix = [letter.lower() for letter in prefix]
#    prefix = ''.join(prefix)
#    return prefix,simplest_name_w_the,simplest_name_wo_the,simplest_name_w_the_wo_news
    
    
#Final Comparator

##################################DEPRECATED FUNCTION
#def URL_Checker(name,URL):
#    prefix, simplest_name_the, simplest_name_wo_the, simplest_name_w_the_wo_news = kwrds_extr(name)
#    if (((prefix in URL) or (simplest_name_the in URL) or (simplest_name_wo_the in URL) or (simplest_name_w_the_wo_news in URL)) and ('facebook' or 'indiatimes') not in URL):
#        return True
#    return False

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
        if(((words[i] in URL) and (words[(i+1)%len(words)] in URL)) and ('facebook' or 'twitter' or 'indiatimes' or 'timesofindia')):
            return True
        elif(i == len(words)-1):
            return False
            
            
    
link = []





for j in range(5):
        if URL_Chckr_w_words_extr(source['NAME'].iloc[0],first5links[j]):
            link.append(first5links[j])
            break
        else:
            link.append(None)
            break
            


#NOW, you can implement all of this, but before this, you should check whether you already contain these IPRD sources are in 
#our FinalDB or not, if not, then use these tools

for i in range(1,len(source)):
    
    input_1 = driver.find_element_by_name("q")  #search bar
    input_1.clear()
    input_1.send_keys('site: ' + list(source.iloc[i])[0] + ' .in news')
    
    search_but = driver.find_elements_by_class_name('Tg7LZd')[0] #search button #wrong search button
    search_but.click()
    time.sleep(0.5)
    sel = Selector(text = driver.page_source)
    first5links = sel.xpath('//*[@class="srg"]/div/div/div/div/a/attribute::href').extract()[:3]    #Extracting the first 3 URLs
    if len(first5links) is 0: #Instead of brute forcing validating that captcha, make a new instance of webdriver and start where you left off
        
        inp = input('Ayy whats happening bruh!? All good???')
        sel = Selector(text = driver.page_source)
        first5links = sel.xpath('//*[@class="srg"]/div/div/div/div/a/attribute::href').extract()[:3]
        
        
        #inp = input('All good!?')
        #sel = Selector(text = driver.page_source)
        #first3links = sel.xpath('//*[@class="srg"]/div/div/div/div/a/attribute::href').extract()[:3]    #Extracting the first 3 URLs
        #curr_index = i 
        
        #I'm just gonna do the captcha
        
        
        
        
        
        
        
        #driver = webdriver.Chrome('chromedriver') # new instance of webdriver
        #driver.get('https://www.google.com/')
        #input_1 = driver.find_element_by_name("q")  #search bar

        #input_1.send_keys('site: ' + list(source.iloc[i])[0] + ' .in news')
        #search_but = driver.find_elements_by_class_name('gNO89b')[1] #search button
        #search_but.click()
        #sel = Selector(text = driver.page_source)
        #first3links = sel.xpath('//*[@class="srg"]/div/div/div/div/a/attribute::href').extract()[:3]    #Extracting the first 3 URLs
        #if len(first3links) is 0:
        #    inp = input('Ayy whats happening bruh!? All good???')
        #    sel = Selector(text = driver.page_source)
        #    first3links = sel.xpath('//*[@class="srg"]/div/div/div/div/a/attribute::href').extract()[:3]    #Extracting the first 3 URLs
        
        
    for j in range(5):
        if URL_Chckr_w_words_extr(source['NAME'].iloc[i],first5links[j]):
            link.append(first5links[j])
            break
        else:
            link.append(None)
            break

arr = pd.DataFrame(link,columns = ['LINKS'])
arr['Name'] = source['NAME']
# WE DON'T WANT FACEBOOK/IndiaTimes PAGES MIND YOU



## FOLLOWING PART IS FOR COMPARING THE IPRD_SOURCES TO FINAL_DB


##IndianNewspapers.in--------->>> FUCKING JACKPOT SON!!!!!!.........