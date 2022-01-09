import tweepy
import autopep8
from humanticfunctions import *
from politwitfunctions import *
import pandas as pd
import http.client
import os
import time
import json
import requests
import sys
import nltk
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')
from nltk.corpus import twitter_samples
import preprocessor as p
import sentiment


analyzer = SentimentIntensityAnalyzer()

query = 'covid'
result = []
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
fvader = open("sentvader.txt", "w", encoding="utf-8")
response = client.search_recent_tweets(query=query, max_results=10)



def tweet_sentiment_hydrate(response):
    analyzer = SentimentIntensityAnalyzer()
    #tweet_sentiment_array = []
    avg_sentiment_array = []
    for tweet in response.data:
        
        clean_tweet = p.clean(tweet.text)
    #result.append(p.clean(tweet_body))
        #tweet_sentiment_array.append(clean_tweet)
    
        vs = (analyzer.polarity_scores(clean_tweet))

        #tweet_sentiment_array.append(vs)
        avg_sentiment_array.append(vs)
        print(clean_tweet)
    #print('vs')
    #print(clean_tweet)
    #print(vs)   
    #polarity_string = ''.join(map(str, vs))
    #arr = np.append([clean_tweet, vs])

    #a_2d_list.append([5, 6])
    #arr2 = np.append(vs)
    #tweetwithsentiment = clean_tweet+polarity_string   
    #fvader.write(tweetwithsentiment)
    #fvader.write(polarity_string)
    #print(len(arr))
    #hhh = analyzer.polarity_scores(avg_sentiment_array[20])
    
    #print(avgsentscores)
    return (avgsentscores)


tweet_sentiment_hydrate(response)
print(h)







    
  
#fvader.close
#print('vs all up')
#print(len(arr))

#print(analyzer.polarity_scores(vs))         

# //todo #5 

#USER_ID = "potus"
#pers = "sales"
#message = result
#makeitastring = ''.join(map(str, message))



#f = open("humantic_tweets.txt", "w", encoding="utf-8")

#f.write(makeitastring)
#f.close()

#fvader.close()


#send_personality_traits(USER_ID, message)


#for x in range(1, 45):

   # time.sleep(1)

   # print('waiting...')



#retrieve_personality_traits(USER_ID, pers)