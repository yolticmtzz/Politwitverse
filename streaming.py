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
        
        ###########################################################################################################################
        query = 'Covid lang:en'
        project = 'Covid Stream test'
        jobtype = "stream"
        ###########################################################################################################################
        
        tweet_id = status.id
        tweet_text = status.text
          
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
        tweet_retweeted = status.retweeted
        tweet_lang = status.lang
        tweet_created_at = status.created_at
        tweet_user_description = status.user.description
        tweet_clean_text = clean_tweets(tweet_text) #
        tweet_sentiment_all = tweet_sentiment_analyzer(tweet_clean_text) #
        tweet_sentiment_compound = tweet_sentiment_all.get('compound') # 
        print(tweet_text)  
        print(tweet_retweeted)
        

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
            INSERT INTO TWEET_ALL_UP (tweet_id, tweet_text, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_screen_name, tweet_username, tweet_geo, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_like_count, tweet_favorited, tweet_retweeted, tweet_lang, tweet_created_at, query, project, tweet_mentions, tweet_hashtags, tweet_urls, tweet_user_description, jobtype, tweet_clean_text, tweet_sentiment_compound) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            tweet_id, tweet_text, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_screen_name, tweet_username, tweet_geo, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_like_count, tweet_favorited, tweet_retweeted, tweet_lang, tweet_created_at, query, project, tweet_mentions, tweet_hashtags, tweet_urls, tweet_user_description, jobtype, tweet_clean_text, tweet_sentiment_compound).rowcount

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
printer.filter(track=['covid'],languages=["en"])
################################################################################################################################