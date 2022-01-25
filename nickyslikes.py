import tweepy
import pyodbc
import textwrap
from twit import *

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAAQ6Wu3fVaVsdg4PHyN7ktSku8u8g%3DMWmLEo5o3YPP0HsKRrX5S1UcKAnemvF2UVPG5Sp6S2qXRFNB9j')

user_id = '4591016128'

response = client.get_liked_tweets(user_id, tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],media_fields=['duration_ms','height','media_key', 'preview_image_url','promoted_metrics','public_metrics','type,url'],place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],max_results=10)

# driver = '{ODBC Driver 17 for SQL Server}'
# server_name = 'twitpoli1984-sqlsrv'
# database_name = 'mosenatetweets-db'
# server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
# username = "joewils"
# password = "Pissyduck113!@"

# connection_string = textwrap.dedent('''
#     Driver={driver};
#     Server={server};
#     Database={database};
#     Uid={username};
#     Pwd={password};
#     Encrypt=yes;
#     TrustServerCertificate=no;
#     Connection Timeout=30;
# '''.format(
#         driver=driver,
#         server=server,
#         database=database_name,
#         username=username,
#         password=password
# ))

# cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
# crsr: pyodbc.Cursor = cnxn.cursor()
for tweet in response.data:
    tweet_text = tweet.text
    tweet_clean_text = clean_tweets(tweet.text)
    tweet_created_at = tweet.created_at
    tweet_id = tweet.id
    tweet_clean_text = clean_tweets(tweet.text)
    if tweet.data['public_metrics']:
        tweet_retweet_count, tweet_like_count, tweet_quote_count, tweet_reply_count = hydrate_public_metrics(tweet.data)
    ref_tweets = tweet.referenced_tweets
    if tweet.referenced_tweets:
        tweet_reference_type, tweet_reference_id = hydrate_referenced_tweets(tweet.referenced_tweets)
    else:
        tweet_reference_type = None
        tweet_reference_id = None
        
    tweet_context_annotations = hydrate_context_annotations(tweet.context_annotations) # make annotations into one function too
    tweet_created_at = tweet.created_at #
    tweet_lang = tweet.lang #
    tweet_reply_settings = tweet.reply_settings #
    tweet_id = tweet.id #
    tweet_source = tweet.source #
    tweet_conversation_id = tweet.conversation_id #
    tweet_text = tweet.text#
    tweet_user = tweet.author_id #
    tweet_in_response_to_user_id = tweet.in_reply_to_user_id #

    
        
    
    


    
    
    
    # # TODO #19 public metrics into a function
    #     public_metrics_dict = (tweet_dict['public_metrics'])
    #     tweet_retweet_count = public_metrics_dict.get('retweet_count') #
    #     tweet_like_count = public_metrics_dict.get('like_count') #
    #     tweet_quote_count = public_metrics_dict.get('quote_count') #
    #     tweet_reply_count = public_metrics_dict.get('reply_count') #{{{{}}}}
    
    

    # crsr.execute(
    #     "SELECT tweet_id, COUNT(*) FROM NICKYSLIKES WHERE tweet_id = ? GROUP BY tweet_id",
    #     (tweet_id)
    # )

    # results = crsr.fetchall()
    # row_count = crsr.rowcount

    # if row_count == 0: # tweet_id (primary key) does not already exit
    #     count = crsr.execute("""
    #     INSERT INTO NICKYSLIKES (tweet_id, tweet_created_at, tweet_text)
    #     VALUES (?,?,?)""",
    #     tweet_id, tweet_created_at, tweet_text).rowcount 
    
    # print("commited to SQL")

# crsr.commit()

# cnxn.close() 
    