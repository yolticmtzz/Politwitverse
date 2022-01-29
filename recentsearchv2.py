import tweepy
import pyodbc
import textwrap
from twit import * # functions used to streamline getting data out of tweet and user payloads
from twitnlp import * # functions used in tweet NLP (sentiment, emotion, hate, etc.)
import time
import os

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("CLIENT_ID")
access_token_secret = os.getenv("CLIENT_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")


def print_tweet_data():
    print(tweet_created_at)
    print(user.name)
    print(tweet.text)
    print(tweet_annotations)
    print(tweet_hashtags)
    print(tweet_urls)
    print(tweet_mentions)
    print("---------------------------------------------------")
    return

client = tweepy.Client(bearer_token=bearer_token)
#client2 = tweepy.Client

###################################################################################################################################
#queries
# user_id = '4591016128'
query = "mogov"
#query = "missouri schools"
project_name = ""
query_name = query
project_type = "batchtoken" # can be batch, stream, batchtoken, batchpaginator

###################################################################################################################################

response = client.search_recent_tweets(query=query, tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],media_fields=['duration_ms','height','media_key', 'preview_image_url','promoted_metrics','public_metrics','type,url'],place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],max_results=100)

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
metadata = response.meta
next_token = metadata.get('next_token')
metadata = response.meta
while next_token is not None:
        users = {u['id']: u for u in response.includes['users']} # iterating through users in payload and adding them to users dict    
        for tweet in response.data:  
            #tweet_dict = tweet.data
            #ent_dict = tweet.entities
            if users[tweet.author_id]:  # many users are included in payload (mentions, etc) this just makes tweet user and user in users be equal
                user = users[tweet.author_id]
            tweet_liked_text = tweet.text
            tweet_created_at = tweet.created_at
            tweet_id = tweet.id
            tweet_clean_text = clean_tweets(tweet.text)
            
            if tweet.data['public_metrics']:
                tweet_retweet_count, tweet_like_count, tweet_quote_count, tweet_reply_count = hydrate_public_metrics(tweet.data)
            ref_tweets = tweet.referenced_tweets
            if tweet.referenced_tweets:
                tweet_reference_type, tweet_reference_id = hydrate_referenced_tweets(tweet.referenced_tweets)
            else:
                tweet_reference_type = "original"
                tweet_reference_id = None
                
            print (tweet_reference_type)
            print (tweet_reference_id)
            
             # TODO #21 Lookup replied or quoted tweet text and insert it into database   
            # if tweet_reference_type:
            #     reftweet = client2.get_tweet(tweet_reference_id) # get referenced tweet text for retweets, replies and quoted tweets - more context
            #     tweet_referenced_text = reftweet.data
            #     tweet_reference_text = makeitastring(tweet_referenced_text)

            # else:
            #     tweet_referenced_text = None
                
            # print(tweet_referenced_text)
            tweet_referenced_text = None
         
                
                
            # populate tweet fields 
            tweet_lang = tweet.lang 
            tweet_reply_settings = tweet.reply_settings 
            tweet_source = tweet.source 
            tweet_conversation_id = tweet.conversation_id 
            tweet_author_id = tweet.author_id 
            tweet_in_response_to_user_id = tweet.in_reply_to_user_id 
            if tweet.entities is not None:
                tweet_mentions, tweet_hashtags, tweet_annotations, tweet_urls = hydrate_entities(tweet.entities)
            tweet_entities, tweet_domains = hydrate_context_annotations(tweet.data) 
            tweet_created_at = tweet.created_at 
            tweet_lang = tweet.lang 
            tweet_reply_settings = tweet.reply_settings 
            tweet_id = tweet.id 
            tweet_source = tweet.source 
            tweet_conversation_id = tweet.conversation_id 
            tweet_author_id = tweet.author_id 
            tweet_in_response_to_user_id = tweet.in_reply_to_user_id 
            
            #populate tweet user fields
            tweet_user_id = user.id            
            tweet_username = str(user.username) # in some rare cases username was coming back as dict type, converting to string
            tweet_user_name = user.name
            tweet_user_description = user.description
            tweet_user_location = user.location
            tweet_user_created_at = user.created_at
            tweet_user_pinned_tweet = user.pinned_tweet_id
            tweet_user_profile_url = user.profile_image_url
            tweet_user_verified = user.verified
            tweet_user_listed_count = user.public_metrics['listed_count']
            tweet_user_following_count = user.public_metrics['following_count']
            tweet_user_followers_count = user.public_metrics['followers_count']
            tweet_user_count = user.public_metrics['tweet_count']
            
            tweet_sentiment_label, tweet_score_probability = tweet_sentiment_analyzer(tweet_liked_text)
            tweet_emotion_label = tweet_emotion_analyzer(tweet_clean_text)
            tweet_hate_label = tweet_hate_analyzer(tweet_clean_text) 

            crsr.execute(
                "SELECT tweet_id, COUNT(*) FROM NICKYSLIKES WHERE tweet_id = ? GROUP BY tweet_id",
                (tweet_id)
            )

            results = crsr.fetchall()
            row_count = crsr.rowcount

            if row_count == 0: # tweet_id (primary key) does not already exit
                count = crsr.execute("""
                INSERT INTO NICKYSLIKES (tweet_liked_text, tweet_created_at, tweet_id, tweet_clean_text, tweet_retweet_count, tweet_like_count, tweet_quote_count, tweet_reply_count, tweet_reference_type, tweet_reference_id, tweet_lang, tweet_reply_settings, tweet_source, tweet_conversation_id, tweet_author_id, tweet_in_response_to_user_id,tweet_user_id, tweet_username, tweet_user_description, tweet_user_location, tweet_user_created_at, tweet_user_pinned_tweet, tweet_user_profile_url, tweet_user_verified, tweet_user_listed_count, tweet_user_following_count, tweet_user_followers_count, tweet_sentiment_label, tweet_emotion_label, tweet_hate_label, tweet_mentions, tweet_hashtags, tweet_annotations, tweet_urls, tweet_entities, tweet_domains, tweet_user_name, tweet_referenced_text, tweet_user_count)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                tweet_liked_text, tweet_created_at, tweet_id, tweet_clean_text, tweet_retweet_count, tweet_like_count, tweet_quote_count, tweet_reply_count, tweet_reference_type, tweet_reference_id, tweet_lang, tweet_reply_settings, tweet_source, tweet_conversation_id, tweet_author_id, tweet_in_response_to_user_id,tweet_user_id, tweet_username, tweet_user_description, tweet_user_location, tweet_user_created_at, tweet_user_pinned_tweet, tweet_user_profile_url, tweet_user_verified, tweet_user_listed_count, tweet_user_following_count, tweet_user_followers_count, tweet_sentiment_label, tweet_emotion_label, tweet_hate_label,tweet_mentions, tweet_hashtags, tweet_annotations, tweet_urls,tweet_entities, tweet_domains, tweet_user_name, tweet_referenced_text, tweet_user_count).rowcount 
            
            crsr.commit()
        
        response = client.search_recent_tweets(query=query, expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'], max_results=100, next_token=next_token, tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'])
        
        metadata = response.meta
        next_token = metadata.get('next_token')
        print('sleeping')
        time.sleep(1)

cnxn.close() 
    