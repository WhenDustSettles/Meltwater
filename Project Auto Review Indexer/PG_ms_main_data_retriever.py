from selenium import webdriver
from parsel import Selector
import csv
good_sents = []
import time
import pandas as pd
from rake_nltk import Rake
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sent_analy_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score
    
def classifier(sentence):
    score = sent_analy_scores(sentence)
    if score['compound'] >=0.05:
        return 1
    elif score['compound'] <=-0.05:
        return -1
    else:
        return 0



driver = webdriver.Chrome('chromedriver')

#####BELOW IS A SENTIMENT (GOOD/BAD) KERYWORDS EXTRACTOR  WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP
analyser = SentimentIntensityAnalyzer()
links = pd.read_csv('ms_rev_link.csv')
URL = links['REVIEW LINKS'].iloc[23]
driver.get(URL)
time.sleep(3)
sel  = Selector(text = driver.page_source)
def sent_keywrd(driver):
    sel  = Selector(text = driver.page_source)
    review = ' '.join(sel.xpath('//*[@id="firstReview"]/div/div[2]/div[2]/div[4]/p/text()').extract())
    rake = Rake()
    rake.extract_keywords_from_text(review)
    kwrds = rake.get_ranked_phrases_with_scores()
    imp_kwrds = [kwrds[i][1] for i in range(len(kwrds)) if kwrds[i][0] >= 4]
    goodness = []
    badness = []
    for kwrd in imp_kwrds:
        if classifier(kwrd) == 1: goodness.append(kwrd)
        elif classifier(kwrd) == -1: badness.append(kwrd)
    return goodness, badness 
    
#####           #######         #####           ######   WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP
time.sleep(3)
sel  = Selector(text = driver.page_source)

#####BELOW IS THE RATINGS RETRIEVER
def final_rating(sel):
    rating = sel.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_litMemRating"]/span/i/attribute::class').extract()
    stars_given = rating.count('icon-rating rated-star')
    total_stars = len(rating)
    return stars_given,total_stars
#####           ######          #####           ######



#####BELOW IS THE RATED KEYWORDS EXTRACTOR #####ALL ARE OUT OF 5
def summary_extr(sel):
    mileage = 5-len(sel.xpath('//*[@id="uniqueRatDiv"]/div/div[1]/div[1]/div/div[2]/div[@class = "unrated-unirating"]').extract())
    comfort = 5-len(sel.xpath('//*[@id="uniqueRatDiv"]/div/div[1]/div[2]/div/div[2]/div[@class = "unrated-unirating"]').extract())
    reliability = 5-len(sel.xpath('//*[@id="uniqueRatDiv"]/div/div[2]/div[1]/div/div[2]/div[@class = "unrated-unirating"]').extract())
    roadgrip = 5-len(sel.xpath('//*[@id="uniqueRatDiv"]/div/div[2]/div[2]/div/div[2]/div[@class = "unrated-unirating"]').extract())
    appeal = 5-len(sel.xpath('//*[@id="uniqueRatDiv"]/div/div[3]/div/div/div[2]/div[@class = "unrated-unirating"]').extract())
    return mileage,comfort,reliability,roadgrip,appeal
    
def pros_con_clf(sel):
    mil,com,rel,rg,app = summary_extr(sel)
    kwrds = {'mileage' : mil,'comfort' : com,'reliability' : rel,'roadgrip' : rg,'appeal' : app}
    pros,cons = [],[]
    for key,val in kwrds.items():
        if val<3:
            cons.append(key)
        else:
            pros.append(key)
    return pros,cons

#####           ######          #####           ######



for i in range(0,50):
    
    #MORE SHIT HERE
    URL = links['REVIEW LINKS'].iloc[i]
    driver.get(URL)
    goodness,badness = sent_keywrd(driver)
    
    with open('ms_activa_rev3.csv','a') as myfile:
        writer = csv.writer(myfile)
        writer.writerow([goodness,badness])
    myfile.close()




