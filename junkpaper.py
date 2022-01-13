import tweepy
from collections import defaultdict
import time
import json
import re
import pickle
import ast
import preprocessor as p
import nltk
import pandas as pd

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def print_tweet_data():
    print(tweet_text)
    print(tweet_sentiment_compound)
    print('\n')
    
def remove_whitespace(text):
    return  " ".join(text.split())

def clean_tweets(tweet_text):
  p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED)
  clean_tweet_text = p.clean(tweet_text)
  #clean_tweet_text = p.parse(clean_text)
  clean_tweeet_text = remove_whitespace(clean_tweet_text)
  return(clean_tweet_text)

#creates a dictionary of positive score, neutral score, negativie score or compound score. Here it is 
def tweet_sentiment_analyzer(clean_text):
  sentiment_scores = []
  sentiment_scores = analyzer.polarity_scores(clean_text)
  return(sentiment_scores)

#using string manipulation to get tweets - tested on all scenarios but could need to be changed if referenced_tweets payload changes
def referenced_hydrate(referenced_tweets):
    t = makeitastring(referenced_tweets)
    t = t.split('=')
    #t = referenced_tweets.split('=')
    tweet_type = t[2].replace(']', ' ')
    tweet_reference_id = t[1].replace(']', ' ').replace(' type', '')
    referenced_tweets_list = []
    referenced_tweets_list.append(tweet_type)
    referenced_tweets_list.append(tweet_reference_id)
    return(referenced_tweets_list)


def annotations_hydrate(entity_list):  
    x = 0 #list index
    i = 1 #list length
    container = []
    entity_length = len(entity_list)
    while i <= entity_length:
        temp_list = entity_list[x]
        t = temp_list.get("type")
        container.append(t)
        n = temp_list.get("normalized_text")                  
        container.append(n)
        i = i + 1
        x = x + 1  
    return container

def mention_hydrate(entity_list):  
    x = 0 #list index
    i = 1 #list length
    container = []
    entity_length = len(entity_list)
    while i <= entity_length:
        temp_list = entity_list[x]
        j = temp_list.get("username")
        container.append(j)
        i = i + 1
        x = x + 1   
    return container

def hashtag_hydrate(entity_list):  
    x = 0 #list index
    i = 1 #list length
    container = []
    entity_length = len(entity_list)
    while i <= entity_length:
        temp_list = entity_list[x]
        j = temp_list.get("tag")
        container.append(j)
        i = i + 1
        x = x + 1  
    return container

def url_hydrate(entity_list):  
    x = 0 #list index
    i = 1 #list length
    container = []
    entity_length = len(entity_list)
    while i <= entity_length:
        temp_list = entity_list[x]
        j = temp_list.get("expanded_url")
        container.append(j)
        i = i + 1
        x = x + 1  
    return container

def makeitastring(wannabestring):
  convertedstring = ''.join(map(str, wannabestring))
  return(convertedstring)

#query filter
#query = '@LaurenArthurMO OR @Dougbeck562 OR @RickBrattin OR @justinbrownmo OR @EricBurlison OR @MikeCierpiot OR @SandyCrawford2 OR @BillEigel OR @SenatorEslinger OR @votegannon OR @DLHoskins OR @lincolnhough OR @Koenig4MO OR @TonyForMissouri OR @KarlaMayMO4 OR @SenAngelaMosley OR @bobondermo OR @gregrazer OR @hrehder OR @RobertsforSTL OR @calebrowden OR @JillSchupp OR @beedubyah1967 OR @BrianWilliamsMO'

query = 'covid -is:retweet'

client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')



response = client.search_recent_tweets(query=query,
                                       tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
                                       user_fields=['created_at','description','entities,id','location,name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
                                       expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],
                                       media_fields=['duration_ms','height','media_key','preview_image_url','promoted_metrics','public_metrics','type,url'],
                                       place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],
                                       poll_fields=['duration_minutes','end_datetime','id,options','voting_status'], 
                                       max_results=10)


ent_dict =  [] #dictionary for entities in response.data
tweet_dict = [] #dictionary for tweets in response.data
referenced_tweets_list = [] 
public_metrics_dict = []
context_annotations_dict = {}
t_mentions = []
t_urls = []
t_annotations = []
t_hashtags = []
user_dict= {}
time.sleep(3)
analyzer = SentimentIntensityAnalyzer()

df = pd.DataFrame()

column_names = ["tweet_id", "tweet_created_at", "tweet_text", "tweet_lang", "tweet_source", "tweet_reply_settings", "tweet_conversation_id",            "tweet_in_response_to_user", "tweet_username", "tweet_user_tweet_count", "tweet_user_description", "tweet_user_location", "tweet_user_created_at", "tweet_user_pinned_tweet", "tweet_user_profile_url", "tweet_user_verified", "tweet_user_listed_count", "tweet_user_following_count", "tweet_user_followers_count", "tweet_reply_count", "tweet_like_count", "tweet_quote_count", "tweet_reply_count", "tweet_reference_type", "tweet_reference_id", "tweet_clean_text", "tweet_sentiment_all", "tweet_sentiment_compound", "tweet_hashtags", "tweet_annotations", "tweet_urls", "tweet_mentions"]

df = pd.DataFrame(columns = column_names)

a = 0 #main loop counter
u = 0


    
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

tweet_user_dict = user_dict
    
