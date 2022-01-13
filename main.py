import tweepy
import autopep8
from humanticfunctions import *
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
from nltk.corpus import twitter_samples
import preprocessor as p
import sentiment
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import datetime
import twitter

def def_value():
    return "Not Present"

def makieitastring(wannabestring):
  convertedstring = ''.join(map(str, wannabestring))
  return(convertedstring)

def hydrate_entities(entities_soup):
  es = []
  for s in range(len(users['Hashtags'])):
      hasht=[]
      for t in range(len(tweets.Hashtags[s])):
         #zx = tweets['Hashtags'][s][t]['text']
         hasht.append(tweets['Hashtags'][s][t]['text'])
         t=t+1
      ht.append(hasht)
      s=s+1
  tweets['HT']=zip(ht)

def hydrate_search_recent_tweet_data(tweet_data):
  user_dict = {}
  tweet_dict = {}
  result = []
  hashtags = []
  for tweet in response:
    # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
    for user in response.includes['users']:
        user_dict[user.id] = {'username': user.username, 
                              'followers': user.public_metrics['followers_count'],
                              'tweets': user.public_metrics['tweet_count'],
                              'description': user.description,
                              'location': user.location,
                              'user_created_at': user.created_at,
                              'pinned_tweet' : user.pinned_tweet_id,
                              'profile_url' : user.url,
                              'verified_status' : user.verified,
                              'listed_count' : user.public_metrics['listed_count']                    
                             }

    for tweet in response.data:
        author_info = user_dict[tweet.author_id]
        tweet_dict.append({
                    'author_id': tweet.author_id, 
                    'username': author_info['username'],
                    'author_followers': author_info['followers'],
                    'author_tweets': author_info['tweets'],
                    'author_description': author_info['description'],
                    'author_location': author_info['location'],
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'retweets': tweet.public_metrics['retweet_count'],
                    'replies': tweet.public_metrics['reply_count'],
                    'likes': tweet.public_metrics['like_count'],
                    'quote_count': tweet.public_metrics['quote_count'],
                    })  

    import pandas as pd
    #print(result)
    return user_dict
        

#analyzer = SentimentIntensityAnalyzer()

#fields to get from search_recent_tweets



#CONSUMER_KEY = 'CwOPV8GflO6ErmPz3oZGzKZnP'
#CONSUMER_SECRET = '1oUytqRLZMaW8BWxQhX3aVVuzjByrTmenP1rwVeBxo4wCSA7WO'
#OAUTH_TOKEN = '1469761271709028359-5x8qQU755HUPv5tvtk8bfQRLYJ7JWV'
#OAUTH_TOKEN_SECRET = 'lpM9w093tgjCHut2guCiarSdlUlJqk593JjWjUGpjbC5L'
#auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
 #                          CONSUMER_KEY, CONSUMER_SECRET)

#twitter_api = twitter.Twitter(auth=auth)

query = 'covid'
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
#fvader = open("sentvader.txt", "w", encoding="utf-8")

#response = client.search_recent_tweets(query=query,
#                                       tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
#                                       user_fields=['created_at','description','entities','id','location,name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
#                                       expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],
#                                       media_fields=['duration_ms','height','media_key','preview_image_url','promoted_metrics','public_metrics','type,url'],
#                                       place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],
#                                       poll_fields=['duration_minutes','end_datetime','id,options','voting_status'], 
#                                       max_results=10)


# Import unquote to prevent URL encoding errors in next_results
from urllib.parse import unquote

# See https://dev.twitter.com/rest/reference/get/search/tweets

tsearch = client.search_recent_tweets(query=query,expansions=['entities.mentions.username'])

