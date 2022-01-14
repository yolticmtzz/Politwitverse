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
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from re import search
#nltk.download('vader_lexicon')

def remove_ASCII(text_soup):
     string_encode = text_soup.encode("ascii", "ignore")
     string_decode = string_encode.decode()
     return(string_decode)

def print_tweet_data():
    print(tweet_id)
    #print(tweet_text)
    #print(tweet_sentiment_compound)
    #print('\n')
    
def remove_whitespace(text):
    return  " ".join(text.split())

def clean_tweets(tweet_text):
  p.set_options(p.OPT.URL, p.OPT.MENTION)
  clean_tweet_text = p.clean(tweet_text)
  #clean_tweet_text = p.parse(clean_text)
  clean_tweeet_text = remove_whitespace(clean_tweet_text)
  return(clean_tweet_text)

#creates a dictionary of positive score, neutral score, negativie score or compound score. Here it is 
def tweet_sentiment_analyzer(clean_text):
  sentiment_scores = []
  sentiment_scores = analyzer.polarity_scores(clean_text)
  return(sentiment_scores)

def hydrate_context(jj): #accepts tweet.annotations and returns a list of annotations, domain ids and entitity ids
    c = makeitastring(jj)
    print('\n')
    context15 = c.replace('"', '')
    context16 = context15.replace('"',"")
    context17 = context16.replace("{", "")
    context18 = context17.replace("}", "")
    context19 = context18.replace("(", "")
    context20 = context19.replace("'", "")
    context21 = context20.replace(")", "")
    context22 = context21.replace(":", ',')
    context2 = context20.split(",")
    context_list = []
    domain_list = []
    entity_list = []
    final_list = []
    i=0
    while i < len(context2):
        temp_context = context2[i]
        if search("Entit", temp_context):
            temp_context = ""
        if search("Entit", temp_context):
            temp_context = ""
        if search("Nelson", temp_context):
            temp_context = ""
        if search(("name: "), temp_context):
            temp_context2 = temp_context.replace("name: ", "")
            context_list.append(temp_context2.strip())
        if search("description: ", temp_context):
            temp_context2 = temp_context.replace("description: ", "")
            context_list.append(temp_context2.strip())
        if search("like ", temp_context):
            temp_context2 = temp_context.replace("like ", "")
            context_list.append(temp_context2.strip())
        if search("domain: id", temp_context):
            temp_context2 = temp_context.replace("domain: id:", "") #see if by changing variables from context2 to something different in each
            print(temp_context2 + '- domain')
            domain_list.append(temp_context2.strip())
        if search("entity: id", temp_context):
            temp_context2 = temp_context.replace("entity: id:", "")
            entity_list.append(temp_context2.strip())
        i=i+1
    
    context_list = list(set(context_list))  
   # print(context_list)
    domain_list = list(set(domain_list)) 
   # print(domain_list)
    entity_list = list(set(entity_list)) 
   # print(entity_list)
    final_list.append(context_list)
    final_list.append(domain_list)
    final_list.append(entity_list)
   
    return(final_list)

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

#query filters
#query = '@LaurenArthurMO OR @Dougbeck562 OR @RickBrattin OR @justinbrownmo OR @EricBurlison OR @MikeCierpiot OR @SandyCrawford2 OR @BillEigel OR @SenatorEslinger OR @votegannon OR @DLHoskins OR @lincolnhough OR @Koenig4MO OR @TonyForMissouri OR @KarlaMayMO4 OR @SenAngelaMosley OR @bobondermo OR @gregrazer OR @hrehder OR @RobertsforSTL OR @calebrowden OR @JillSchupp OR @beedubyah1967 OR @BrianWilliamsMO -is:retweet'

#query = 'missouri education -is:retweet'

query = "from:tonylovasco OR from:gowestformo OR from:davegriffithmo OR from:VeitRudy OR from:reedyhouserep OR from:MikeHaffnerMO OR from:rogers4missouri OR from:MarkEllebracht OR from:MaggieforMO OR from:Ashley4MO OR from:PoucheSean OR from:JoshHurlbert OR from:Repdistrict10 OR from:rep_rusty OR from:edlewis_g from:mmcgirl1 OR from:CourtwayCyndi OR from:danshaul113 OR from:RobVescovo OR from:NickBSchroer OR from:AJSchwadron OR cody4mo OR from:BenBakerMO OR from:DirkEDeaton"

#query = "moleg -is:retweet"


client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

 
#response = client.search_recent_tweets(query=query,tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location,name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],media_fields=['duration_ms','height','media_key', 'preview_image_url','promoted_metrics','public_metrics','type,url'],place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],max_results=100)

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
analyzer = SentimentIntensityAnalyzer()
df = pd.DataFrame()

tweet_column_names = ["tweet_id", "tweet_created_at", "tweet_text", "tweet_lang", "tweet_source", "tweet_reply_settings", "tweet_conversation_id", "tweet_in_response_to_user_id", "tweet_username", "tweet_user_tweet_count", "tweet_user_description", "tweet_user_location", "tweet_user_created_at", "tweet_user_pinned_tweet", "tweet_user_profile_url", "tweet_user_verified", "tweet_user_listed_count", "tweet_user_following_count", "tweet_user_followers_count", "tweet_reply_count", "tweet_like_count", "tweet_quote_count", "tweet_reply_count", "tweet_reference_type", "tweet_reference_id", "tweet_clean_text", "tweet_sentiment_all", "tweet_sentiment_compound", "tweet_hashtags", "tweet_annotations", "tweet_urls", "tweet_mentions", "tweet_user_id", "tweet_context_annotations", "tweet_domain_ids", "tweet_entity_ids"]

df = pd.DataFrame(columns = tweet_column_names)

response = client.search_recent_tweets(query=query,tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],media_fields=['duration_ms','height','media_key', 'preview_image_url','promoted_metrics','public_metrics','type,url'],place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],max_results=20)

   
users = {u['id']: u for u in response.includes['users']}         
for tweet in response.data:  
    tweet_dict = tweet.data
    ent_dict = tweet.entities
    #print(tweet.author_id)
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        ent_dict = []
        tweet_dict = tweet.data
        ent_dict = tweet.entities

    if 'public_metrics' in tweet_dict:
                public_metrics_dict = (tweet_dict['public_metrics'])
                tweet_retweet_count = public_metrics_dict.get('retweet_count') #
                tweet_like_count = public_metrics_dict.get('like_count') #
                tweet_quote_count = public_metrics_dict.get('quote_count') #
                tweet_reply_count = public_metrics_dict.get('reply_count') #
    else:
        tweet_retweet_count = None
        tweet_like_count = None
        tweet_quote_count = None
        tweet_reply_count = None    
                                
#assign referenced_tweets
    tweet_reference_soup = tweet.referenced_tweets
    if tweet_reference_soup is not None:
            tweet_reference = referenced_hydrate(tweet_reference_soup)
            tweet_reference_type = tweet_reference[0] #
            tweet_reference_id = tweet_reference[1] #
    else:
            tweet_reference_type = None
            tweet_reference_id = None

    #assign context_annotations
    tweet_context_annotations = tweet.context_annotations
    temp_tweet_context_annotations= hydrate_context(tweet.context_annotations) #returns list of contexts, domain ids, and entity ids
    
    if len(temp_tweet_context_annotations[0]) > 0:
        tweet_annotations = temp_tweet_context_annotations[0]
    else:
        tweet_annotations = ""
        
    if len(temp_tweet_context_annotations[1]) > 0:
        tweet_domain_ids = temp_tweet_context_annotations[1]
    else:
        tweet_domain_ids = ""
    
    if len(temp_tweet_context_annotations[2]) > 0:
        tweet_entity_ids = temp_tweet_context_annotations[2]
    else:
        tweet_entity_ids = ""
        
    #domain_ids = temp_tweet_context_annotations[1]
    #entity_ids = temp_tweet_context_annotations[2]
    

    #assign tweet_fields 
    tweet_created_at = tweet.created_at #
    tweet_lang = tweet.lang #
    tweet_reply_settings = tweet.reply_settings #
    tweet_id = tweet.id #
    tweet_source = tweet.source #
    tweet_conversation_id = tweet.conversation_id #
    tweet_text = tweet.text.encode('utf-8') #
    tweet_user = tweet.author_id #
    tweet_in_response_to_user_id = tweet.in_reply_to_user_id #
        
    ######These two functions while separate should be ran together; however instead of creating one function want the option to just get back clean text
    tweet_clean_text = clean_tweets(tweet.text) #
    tweet_sentiment_all = tweet_sentiment_analyzer(tweet_clean_text) #
    tweet_sentiment_compound = tweet_sentiment_all.get('compound') #   
    print(tweet_sentiment_all)                           

    #assign user fields to tweet 
    tweet_user_id = user.id            
    tweet_username = user.username
    tweet_user_tweet_count = user.public_metrics['tweet_count']
    tweet_user_description = user.description
    tweet_user_location = user.location
    tweet_user_created_at = user.created_at
    tweet_user_pinned_tweet = user.pinned_tweet_id
    tweet_user_profile_url = user.profile_image_url
    tweet_user_verified = user.verified
    tweet_user_listed_count = user.public_metrics['listed_count']
    tweet_user_following_count = user.public_metrics['following_count']
    tweet_user_followers_count = user.public_metrics['followers_count']   

    
    #print(ent_dict)
    if 'mentions' in ent_dict:
            t_mentions = ent_dict.get('mentions')
            tweet_mentions = mention_hydrate(t_mentions) #
            
    else:
            tweet_mentions = None
                
                
    if 'hashtags' in ent_dict is not None: #is not None needed????
            t_hashtags = ent_dict.get('hashtags')  
            tweet_hashtags = hashtag_hydrate(t_hashtags) #
                
    else:
            tweet_hashtags = None

    if 'annotations' in ent_dict:
            t_annotations = ent_dict.get('annotations')   
            tweet_annotations = annotations_hydrate(t_annotations) #

    else:
            tweet_annotations = None

    if 'urls' in ent_dict:
            t_urls = ent_dict.get('urls')
            tweet_urls = url_hydrate(t_urls) #
    else:
            tweet_urls = None     

    new_row = {"tweet_id":tweet_id, "tweet_created_at":tweet_created_at, "tweet_text":tweet_text, "tweet_lang":tweet_lang, "tweet_source":tweet_source, "tweet_reply_settings":tweet_reply_settings, "tweet_conversation_id":tweet_conversation_id,"tweet_in_response_to_user_id":tweet_in_response_to_user_id,"tweet_username":tweet_username, "tweet_user_tweet_count":tweet_user_tweet_count, "tweet_user_description":tweet_user_description, "tweet_user_location":tweet_user_location, "tweet_user_created_at":tweet_user_created_at, "tweet_user_pinned_tweet":tweet_user_pinned_tweet, "tweet_user_profile_url":tweet_user_profile_url, "tweet_user_verified":tweet_user_verified, "tweet_user_listed_count":tweet_user_listed_count, "tweet_user_following_count":tweet_user_following_count, "tweet_user_followers_count":tweet_user_followers_count, "tweet_reply_count":tweet_reply_count, "tweet_like_count":tweet_like_count, "tweet_quote_count":tweet_quote_count,  "tweet_reference_type":tweet_reference_type, "tweet_reference_id":tweet_reference_id, "tweet_clean_text":tweet_clean_text, "tweet_sentiment_all":tweet_sentiment_all, "tweet_sentiment_compound":tweet_sentiment_compound, "tweet_hashtags":tweet_hashtags, "tweet_annotations":tweet_annotations, "tweet_urls":tweet_urls, "tweet_mentions":tweet_mentions,"tweet_user_id":tweet_user_id, "tweet_context_annotations":tweet_context_annotations,
    "tweet_domain_ids":tweet_domain_ids, "tweet_entity_ids":tweet_entity_ids}
    
    #print_tweet_data()    
    #append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    

           
#df.to_csv('reps5.csv', index=False)

print('Thank you for using Politwit1984.')        