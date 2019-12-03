from __future__ import division
import operator
import nltk
import string

def isPunct(word):
    return len(word) == 1 and word in string.punctuation

def isNumeric(word):
    try:
        float(word) if '.' in word else int(word)
        return True
    except ValueError:
        return False
        
        
class RakeKeywordExtractor:
    
    def __init__(self):
        self.stopwords = set(nltk.corpus.stopwords.words())
        self.top_fraction = 1 #we will consider top 3 candidates later
        
    def _generate_candidate_keywords(self,sentences):
        phrase_list = []
        for sentence in sentences:
            words = map(lambda x: '|' if x in self.stopwords else x,nltk.word_tokenize(sentence.lower()))
            phrase = []
            for word in words:
                if word == '|' or isPunct(word):
                    if len(phrase) > 0:
                        phrase_list.append(phrase)
                        phrase = []
                else :
                    phrase.append(word)
        return phrase_list
        
    def _calculate_word_scores(self, phrase_list):
        word_freq  = nltk.FreqDist()
        word_degree = nltk.FreqDist()
        for phrase in phrase_list:
            degree = len(list(filter(lambda x: not isNumeric(x),phrase))) - 1
            for word in phrase:
                word_freq[word] += 1
                word_degree[word] += degree
        for word in word_freq.keys():
            word_degree[word] = word_degree[word] + word_freq[word]
        word_scores = {}
        for word in word_freq.keys():
            word_scores[word] = word_degree[word]/word_freq[word]
        return word_scores
        
    def _calculate_phrase_scores(self,phrase_list, word_scores):
        phrase_scores ={}
        for phrase in phrase_list:
            phrase_score = 0
            for word in phrase:
                phrase_score += word_scores[word]
            phrase_scores[' '.join(phrase)] = phrase_score
        return phrase_scores
    
    def extract(self,text,incl_scores = False):
        sentences = nltk.sent_tokenize(text)
        phrase_list = self._generate_candidate_keywords(sentences)
        word_scores = self._calculate_word_scores(phrase_list)
        phrase_scores = self._calculate_phrase_scores(phrase_list,word_scores)
        sorted_phrase_scores = sorted(phrase_scores.items(), key = operator.itemgetter(1), reverse  = True)
        n_phrases = len(sorted_phrase_scores)
        #below part is copied, took a lot of time to figure it
        if incl_scores:
            return sorted_phrase_scores[0:int(n_phrases/self.top_fraction)]
        else:
            return map(lambda x: x[0],
            sorted_phrase_scores[0:int(n_phrases/self.top_fraction)])
            
            
rake = RakeKeywordExtractor()
kwrds = rake.extract("""While everyone these days wants to get an electric bike to contribute towards a clean environment.

So I got a Hero Electric Scooter, but let me tell you, service will be a big problem.

The dealers and company employees have no professionalism in their dealings, will promise the moon when you buy.

But when it comes to honouring those, you'd be left running from pillar to post.

Also it is a real pain and impossible to get any one to service, should it fail in the middle of something.

So reliability and servicing is a big issue. Please be aware.

But otherwise the concept is good.""", incl_scores=True)

