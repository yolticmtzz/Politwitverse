import tweepy
from collections import defaultdict
import time
import json
import re
import pickle
import ast

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

query = 'missouri covid -is:retweet'
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

response = client.search_recent_tweets(
                                        query=query,
                                        tweet_fields=['referenced_tweets,entities'],
                                        expansions=['author_id'], 
                                        user_fields=['created_at','description','entities','id,location','name','pinned_tweet_id','profile_image_url','protected','public_metrics','url','username','verified','withheld'],max_results=100)


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

a = 0 #main loop counter

while a < 10:
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
        #print(tweet.data)
        
        tweet_dict = tweet.data
        if 'public_metrics' in tweet_dict:
            public_metrics_dict = (tweet_dict['public_metrics'])
     
            #assign public_metrics
            tweet_retweet_count = public_metrics_dict.get('retweet_count')
            tweet_like_count = public_metrics_dict.get('like_count')
            tweet_quote_count = public_metrics_dict.get('quote_count')
            tweet_reply_count = public_metrics_dict.get('reply_count')
                
        #assign referenced_tweets
        tweet_reference_soup = tweet.referenced_tweets
        print(tweet.referenced_tweets)
        if tweet_reference_soup is not None:
            print("referenced tweet exists")
            tweet_reference = referenced_hydrate(tweet_reference_soup)
            tweet_reference_type = tweet_reference[0]
            tweet_reference_id = tweet_reference[1]
            print(tweet_reference_type)
            print(tweet_reference_id)
        else:
            print("referenced tweets does not exist")

        #assign context_annotations
        tweet_context_annotations = tweet.context_annotations #list need to break it out
 
        #assign tweet_fields 
        tweet_created_at = tweet.created_at
        tweet_lang = tweet.lang
        tweet_reply_settings = tweet.reply_settings
        tweet_id = tweet.id
        tweet_source = tweet.source
        tweet_authoer_id = tweet.author_id
        tweet_conversation_id = tweet.conversation_id
        tweet_text = tweet.text
        tweet_user = tweet.author_id
        tweet_in_response_to_user_id = tweet.in_reply_to_user_id
        
        #assign user fields to tweet                      
        tweet_username = author_info['username']
        tweet_user_tweet_count = user.public_metrics['tweet_count']
        tweet_user_description = user.description
        tweet_user_location = user.location
        tweet_user_created_at = user.created_at
        tweet_user_pinned_tweet = user.pinned_tweet_id
        tweet_user_profile_url = user.url
        tweet_user_verified = user.verified
        tweet_user_listed_count = user.public_metrics['listed_count']
        tweet_user_following_count = user.public_metrics['following_count']
        tweet_user_followers_count = user.public_metrics['followers_count']
   
        ent_dict = tweet.entities

        if bool(ent_dict):
            if 'mentions' in ent_dict:
                print("mentions exists")
                t_mentions = ent_dict.get('mentions')
                tweet_mentions = mention_hydrate(t_mentions)
                print(tweet_mentions)
            else:
                print("mentions does not exist")
            
            
            if 'hashtags' in ent_dict is not None: #is not None needed????
                print("hashtags exists")
                t_hashtags = ent_dict.get('hashtags')  
                tweet_hashtags = hashtag_hydrate(t_hashtags)
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
        print(tweet_text)
        print("username " + tweet_username )
        print("user description " +tweet_user_description)
        print(tweet_user_listed_count)
        print(tweet_user_location)
        print(tweet_user_following_count)
        print(tweet_user_followers_count)
        print(tweet_context_annotations)
        print('\n')
        
print("ENDINGENDINGENDING")
    