import datetime, re, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk.corpus import reuters


stemmer  = SnowballStemmer('english')
def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

token_dict = {}
for article in reuters.fileids():
    token_dict[article] = reuters.raw(article)
    
tfidf = TfidfVectorizer(tokenizer=tokenize_and_stem, stop_words='english', decode_error='ignore')

print ('building term-document matrix... [process started: ' + str(datetime.datetime.now()) + ']')
sys.stdout.flush()

tdm = tfidf.fit_transform(token_dict.values()) # this can take some time (about 60 seconds on my machine)
print ('done! [process finished: ' + str(datetime.datetime.now()) + ']')





from random import randint

feature_names = tfidf.get_feature_names()
print('TDM contains ' + str(len(feature_names)) + ' terms and ' + str(tdm.shape[0]) + ' documents')

print ('first term: ' + feature_names[0])
print ('last term: ' + feature_names[len(feature_names) - 1])

for i in range(0, 4):
    print ('random term: ' + feature_names[randint(1,len(feature_names) - 2)])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import math
from __future__ import division

article_id = randint(0, tdm.shape[0] - 1)
article_text = reuters.raw(reuters.fileids()[article_id])

article_text = '''Hey friends I am sharing my own review on Honda Activa so this is a very bad activa scooter. Its performance is very bad . It also doesn't have a good mileage mileage is approx 25 to 35 km/l. Only and other companies are giving mileage approx 50 km/l.

This is a very dissatisfied vehicle suspension is also very bad it will be good for a month or more but after some time the suspension will make noise tooo much and when you visit the workshop for correcting the noise of activa they didn't able to find the problem.

The sound is very much irritating . Braking system also very bad that you can run into an accident.Tires are very slipy.

There is not much vibration in body then also you didn't feel comfortable while riding this vehicle.

Engine performance also very poor.

Pickup is very low and body is made of very low quality metal.

So overall experience is very bad so I would not suggest anyone to buy this activa.

So according to my suggestion I would not prefer anyone to buy this you can think about any other vehicle. '''

sent_scores = []
for sentence in nltk.sent_tokenize(article_text):
    score = 0
    sent_tokens = tokenize_and_stem(sentence)
    for token in (t for t in sent_tokens if t in feature_names):
        score += tdm[article_id, feature_names.index(token)]
    sent_scores.append((score / len(sent_tokens), sentence))

summary_length = int(math.ceil(len(sent_scores) / 5))
sent_scores.sort(key=lambda sent: sent[0], reverse=True)

print ('*** SUMMARY ***')
for summary_sentence in sent_scores[:summary_length]:
    print (summary_sentence[1])

print ('\n*** ORIGINAL ***')
print (article_text)
    

    