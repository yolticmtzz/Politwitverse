# created_at : The time the status was posted.
# id : The ID of the status.
# id_str : The ID of the status as a string.
# text : The text of the status.
# entities : The parsed entities of the status such as hashtags, URLs etc.
# source : The source of the status.
# source_url : The URL of the source of the status.
# in_reply_to_status_id : The ID of the status being replied to.
# in_reply_to_status_id_str : The ID of the status being replied to in as a string.
# in_reply_to_user_id : The ID of the user being replied to.
# in_reply_to_user_id_str : The ID of the user being replied to as a string.
# in_reply_to_screen_name : The screen name of the user being replied to
# user : The User object of the poster of the status.
# geo : The geo object of the status.
# coordinates : The coordinates of the status.
# place : The place of the status.
# contributors : The contributors of the status.
# is_quote_status : Indicates whether the status is a quoted status or not.
# retweet_count : The number of retweets of the status.
# favorite_count : The number of likes of the status.
# favorited : Indicates whether the status has been favourited by the authenticated user or not.
# retweeted : Indicates whether the status has been retweeted by the authenticated user or not.
# possibly_sensitive : Indicates whether the status is sensitive or not.
# lang : The language of the status. 

# SELECT TOP (1000) [tweet_created_at]
#       ,[tweet_id] #
#       ,[tweet_text] #
#       ,[tweet_lang] #
#       ,[tweet_source] #
#       ,[tweet_reply_settings]
#       ,[tweet_conversation_id]
#       ,[tweet_in_repsonse_to_user_id]
#       ,[tweet_username] #
#       ,[tweet_user_tweet_count]
#       ,[tweet_user_description] #
#       ,[tweet_user_created_at]
#       ,[tweet_user_location]
#       ,[tweet_user_pinned_tweet]
#       ,[tweet_user_profile_url]
#       ,[tweet_user_verified] #
#       ,[tweet_user_listed_count]
#       ,[tweet_user_following_count]
#       ,[tweet_user_followers_count]
#       ,[tweet_reply_count]
#       ,[tweet_like_count]
#       ,[tweet_quote_count]
#       ,[tweet_reference_type]
#       ,[tweet_reference_id]
#       ,[tweet_clean_text]
#       ,[tweet_sentiment_all]
#       ,[tweet_sentiment_compound]
#       ,[tweet_hashtags]
#       ,[tweet_urls]
#       ,[tweet_annotations]
#       ,[tweet_mentions]
#       ,[tweet_user_id]
#       ,[tweet_context_annotations]
#       ,[tweet_domain_ids]
#       ,[tweet_entity_ids]
#       ,[query]
#       ,[project]
#       ,[tweet_entities]
#       ,[tweet_source_url]
#       ,[tweet_in_reply_to_status_id]
#       ,[tweet_in_reply_to_screen_name]
#       ,[tweet_user]
#       ,[tweet_geo]
#       ,[tweet_coordinates]
#       ,[tweet_place]
#       ,[tweet_is_quote_status]
#       ,[tweet_retweet_count]
#       ,[tweet_favorited]
#       ,[tweet_retweeted]
#       ,[jobtype]
#   FROM [dbo].[tweet_all_up]

# { "user": {
#     "id": 6253282,
#     "id_str": "6253282",
#     "name": "Twitter API",
#     "screen_name": "TwitterAPI",
#     "location": "San Francisco, CA",
#     "url": "https://developer.twitter.com",
#     "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
#     "verified": true,
#     "followers_count": 6129794,
#     "friends_count": 12,
#     "listed_count": 12899,
#     "favourites_count": 31,
#     "statuses_count": 3658,
#     "created_at": "Wed May 23 06:01:13 +0000 2007",
#     "utc_offset": null,
#     "time_zone": null,
#     "geo_enabled": false,
#     "lang": "en",
#     "contributors_enabled": false,
#     "is_translator": false,
#     "profile_background_color": "null",
#     "profile_background_image_url": "null",
#     "profile_background_image_url_https": "null",
#     "profile_background_tile": null,
#     "profile_link_color": "null",
#     "profile_sidebar_border_color": "null",
#     "profile_sidebar_fill_color": "null",
#     "profile_text_color": "null",
#     "profile_use_background_image": null,
#     "profile_image_url": "null",
#     "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
#     "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
#     "default_profile": false,
#     "default_profile_image": false,
#     "following": null,
#     "follow_request_sent": null,
#     "notifications": null
#   }
# }

from sqlalchemy import null
import tweepy
import pandas as pd
import csv
import textwrap
import pyodbc
import datetime
import preprocessor as p
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

API_KEY = "anvCaAUUuYqG3xLR7dNAzR0dr"
API_SECRET_KEY = "ULtEkEdycJzC08cyebSg1ExdOVgCg5pUG0qtLPnLta24ClNDqr"
ACCESS_TOKEN = "1469761271709028359-FrJt9sku3toFacDx1tdvmSPc273pKf"
ACCESS_TOKEN_SECRET = "mlblwNEQ21A6IrmC4boX42Rctpq0WLNMfTsoOSmOwPrAa"      
        
stream = tweepy.Stream(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)



class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        if hasattr(status, "retweeted_status"):  # Check if Retweet
            try:
                print(status.retweeted_status.extended_tweet["full_text"])
                tweet_text = status.retweeted_status.extended_tweet["full_text"]
                tweet_retweeted = "TRUE"
                print("retweeted")
            except AttributeError:
                print(status.retweeted_status.text)
                tweet_text = status.retweeted_status.text
                tweet_retweeted = "TRUE"
                print("retweeted")
        else:
            try:
                print(status.extended_tweet["full_text"])
                tweet_text = status.extended_tweet["full_text"]
                tweet_retweeted = "FALSE"
                print("Original Tweet")
            except AttributeError:
                print(status.text)
                tweet_text = status.text
                tweet_retweeted = "FALSE"
                print("Original Tweet")
        
        ###########################################################################################################################
        query = 'missouri education lang:en'
        project = 'missouri education intelligence'
        jobtype = "stream"
        ###########################################################################################################################
        
        tweet_id = status.id
        #tweet_text = status.text #handling above
          
        ent_dict = status.entities
        #place_dict = status.place

        if 'user_mentions' in ent_dict:
            t_mentions = ent_dict.get('user_mentions')
            tweet_mentions = mention_hydrate(t_mentions) #
            tweet_mentions = makeitastring(tweet_mentions)
            
        else:
            tweet_mentions = None
                
                
        if 'hashtags' in ent_dict: 
            t_hashtags = ent_dict.get('hashtags')  
            tweet_hashtags = hashtag_hydrate(t_hashtags) 
            tweet_hashtags = makeitastring(tweet_hashtags)
                
        else:
            tweet_hashtags = None

        # if place_dict:
        #     t_place = place_dict.get('full_name')   
        #     tweet_place = place_hydrate(t_place) 
        #     tweet_place = makeitastring(tweet_place)
              
        # else:
        #     tweet_place = None

        if 'urls' in ent_dict:
            t_urls = ent_dict.get('urls')
            tweet_urls = url_hydrate(t_urls) 
            tweet_urls = makeitastring(tweet_urls)
        else:
            tweet_urls = None     
        
        
        tweet_source = status.source
        tweet_source_url = status.source_url
        tweet_in_reply_to_status_id = status.in_reply_to_status_id
        tweet_in_response_to_user_id = status.in_reply_to_user_id
        tweet_in_reply_to_screen_name = status.in_reply_to_screen_name
        tweet_username = status.user.screen_name
        tweet_user_location = status.user.location
        tweet_user = status.user
        tweet_geo = status.geo
        tweet_coordinates = status.coordinates
        tweet_place = status.place
        tweet_is_quote_status = status.is_quote_status
        tweet_retweet_count = status.retweet_count
        tweet_like_count = status.favorite_count
        tweet_favorited = status.favorited
        tweet_lang = status.lang
        tweet_created_at = status.created_at
        tweet_user_description = status.user.description
        tweet_clean_text = clean_tweets(tweet_text) #
        tweet_sentiment_all = tweet_sentiment_analyzer(tweet_clean_text) #
        tweet_sentiment_compound = tweet_sentiment_all.get('compound') # 
        tweet_user_verified = status.user.verified

        

        print('\n')

        
        #checking for tweet_id since it is primary key
        crsr.execute(
            "SELECT tweet_id, COUNT(*) FROM tweet_all_up WHERE tweet_id = ? GROUP BY tweet_id",
            (tweet_id)
        )
        results = crsr.fetchall()
        row_count = crsr.rowcount
        # print("number of affected rows: {}".format(row_count))
        if row_count == 0:
            #print("It Does Not Exist")    
            count = crsr.execute("""
            INSERT INTO TWEET_ALL_UP (tweet_id, tweet_text, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_screen_name, tweet_username, tweet_geo, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_like_count, tweet_favorited, tweet_retweeted, tweet_lang, tweet_created_at, query, project, tweet_mentions, tweet_hashtags, tweet_urls, tweet_user_description, jobtype, tweet_clean_text, tweet_sentiment_compound, tweet_user_verified) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            tweet_id, tweet_text, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_screen_name, tweet_username, tweet_geo, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_like_count, tweet_favorited, tweet_retweeted, tweet_lang, tweet_created_at, query, project, tweet_mentions, tweet_hashtags, tweet_urls, tweet_user_description, jobtype, tweet_clean_text, tweet_sentiment_compound, tweet_user_verified).rowcount

            #removing tweet_entities, tweet_user (can pull individual attributes), tweet_in_response_to_user_id (dict can't be inserted into SQL), tweet_place

        #print('Rows inserted: ' + str(count))
            
        crsr.commit()

        # cnxn.close()



printer = IDPrinter(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)


driver = '{ODBC Driver 17 for SQL Server}'
server_name = 'twitpoli1984-sqlsrv'
database_name = 'mosenatetweets-db'
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
username = "joewils"
password = "Pissyduck113!@"

connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
        driver=driver,
        server=server,
        database=database_name,
        username=username,
        password=password
))

cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
crsr: pyodbc.Cursor = cnxn.cursor()


def place_hydrate(entity_list):  
    x = 0 #list index
    i = 1 #list length
    container = []
    entity_length = len(entity_list)
    while i <= entity_length:
        temp_list = entity_list[x]
        t = temp_list.get("full_name")
        container.append(t)
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
        j = temp_list.get("screen_name")
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
        j = temp_list.get("text")
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
    convertedstring = ','.join(map(str, wannabestring))
    return(convertedstring)

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

ent_dict = []
analyzer = SentimentIntensityAnalyzer()

################################################################################################################################
printer.filter(track=['missouri education'],languages=["en"])
################################################################################################################################