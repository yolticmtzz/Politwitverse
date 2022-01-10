import tweepy
from collections import defaultdict
import time
import json
import re
import pickle
import ast


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

query = 'missouri schools'
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

#response = client.search_recent_tweets(query=query, tweet_fields=['entities'], max_results=100)
response = client.search_recent_tweets(query=query,
                                       tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
                                        user_fields=['created_at','description','entities','id','location,name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
                                        expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],
                                        media_fields=['duration_ms','height','media_key','preview_image_url','promoted_metrics','public_metrics','type,url'],
                                        place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],
                                        poll_fields=['duration_minutes','end_datetime','id,options','voting_status'], 
                                        max_results=10)

ent_dict = {}
t_mentions = []
t_urls = []
t_annotations = []
t_hashtags = []
time.sleep(3)
a = 0
while a < 10:
    for tweet in response.data: 
        id = tweet.id
        ent_dict = tweet.entities
        print(tweet.id)
        print(tweet.created_at)
        print(tweet.text)
        print(tweet.source)

        if 'mentions' in ent_dict:
            print("mentions exists")
            t_mentions = ent_dict.get('mentions')
            tweet_mentions = mention_hydrate(t_mentions)
            print(tweet_mentions)
        else:
            print("mentions does not exist")
            
            
        if 'hashtags' in ent_dict:
            print("hashtags exists")
            t_hashtags = ent_dict.get('hashtags')   
            tweet_hashtags = mention_hydrate(t_hashtags)
            print(tweet_hashtags)
        else:
            print("hashtags does not exist")

        if 'annotations' in ent_dict:
            print("annotations exists")
            t_annotations = ent_dict.get('annotations')   
            tweet_annotations = annotations_hydrate(t_annotations)
            print(tweet_annotations)
        else:
            print("annotations does not exist")

        if 'urls' in ent_dict:
            print("urls exists")
            t_urls = ent_dict.get('urls')
            tweet_urls = url_hydrate(t_urls)
            print(tweet_urls)

        else:
            print("urls does not exist")
        a = a + 1
        print('\n')
        
print("ENDINGENDINGENDING")
    