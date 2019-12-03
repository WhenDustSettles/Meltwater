from rake_nltk import Rake
r = Rake()
mytext = '''While everyone these days wants to get an electric bike to contribute towards a clean environment.

So I got a Hero Electric Scooter, but let me tell you, service will be a big problem.

The dealers and company employees have no professionalism in their dealings, will promise the moon when you buy.

But when it comes to honouring those, you'd be left running from pillar to post.

Also it is a real pain and impossible to get any one to service, should it fail in the middle of something.

So reliability and servicing is a big issue. Please be aware.

But otherwise the concept is good.'''


kwrds = r.extract_keywords_from_text(mytext)

r.get_ranked_phrases()

