from selenium import webdriver
from parsel import Selector
import pandas as pd

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.bikewale.com/heroelectric-bikes/flash/reviews/')
sel = Selector(text = driver.page_source)
all_rev = sel.xpath('//*[@id="modelReviewsListing"]/div[1]/div/div[3]/ul/li/div[1]/div[1]/a/attribute::href').extract()

pages = ['https://www.bikewale.com/heroelectric-bikes/flash/reviews/page/' + str(i) for i in range(2,8) ]
for page in pages:
    driver.get(page)
    sel = Selector(text = driver.page_source)
    all_rev.extend(sel.xpath('//*[@id="modelReviewsListing"]/div[1]/div/div[3]/ul/li/div[1]/div[1]/a/attribute::href').extract())
    
    
    
    
all_rev_links = ['https://www.bikewale.com' + link for link in all_rev]

#TO TAKE OUT RATINGS AND SUMMARISED RATINGS
#FIRST, FOR RATINGS
# Let's go to the review first 
all_summ_ratings = []
all_fin_ratings = []
for i in range(3):
    link = all_rev_links[i]
    driver.get(link)
    sel = Selector(text = driver.page_source)
    pane = sel.xpath('/html/body/section[2]/div/div[1]/div/div[2]/div[1]/div[2]/ul')
    nums = sel.xpath('/html/body/section[2]/div/div[1]/div/div[2]/div[1]/div[2]/ul/li/div/p/text()').extract()
    summary = sel.xpath('/html/body/section[2]/div/div[1]/div/div[2]/div[1]/div[2]/ul/li/p/text()').extract()
    ratings = dict(zip(summary,nums))
    all_summ_ratings.append(ratings)
    all_fin_ratings.extend(sel.xpath('/html/body/section[2]/div/div[1]/div/div[2]/div[1]/div[1]/span[1]/text()').extract())
    
    
ratings_df = pd.DataFrame(all_summ_ratings)
ratings_df['Final'] = pd.Series(all_fin_ratings)
#KEEP ADDING TO THIS DATAFRAME THE LINKS AND THE KEYWORDS THAT YOU SHOULD EXTRACT FROM YOUR EXTRACTOR
