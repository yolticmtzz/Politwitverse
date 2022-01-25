import tweepy
from collections import defaultdict
import preprocessor as p
import pandas as pd
import re
from re import search
import textwrap
import pyodbc
import nltk
from pysentimiento import create_analyzer
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import twit
import spacy

b_analyzer_sentiment = create_analyzer(task="sentiment", lang="en")
b_analyzer_emotion = create_analyzer(task="emotion", lang="en")
b_analyzer_hate = create_analyzer(task="hate_speech", lang="en")
v_analyzer_sentiment = SentimentIntensityAnalyzer()
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAAQ6Wu3fVaVsdg4PHyN7ktSku8u8g%3DMWmLEo5o3YPP0HsKRrX5S1UcKAnemvF2UVPG5Sp6S2qXRFNB9j')
p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
TweetTokenizer()
stop_words = set(stopwords.words('english'))
nlp = spacy.load('en_core_web_sm')

def has_value(cursor, table, column, value):
    query = 'SELECT 1 from {} WHERE {} = ? LIMIT 1'.format(table, column)
    return cursor.execute(query, (value,)).fetchone() is not None

def remove_ASCII(text_soup):
     string_encode = text_soup.encode("ascii", "ignore")
     string_decode = string_encode.decode()
     return(string_decode)

def print_tweet_data():
    print('--------------------------------------------------------------------------------------------')
    print(tweet_username)
    print(tweet_clean_text)
    print(tweet_sentiment_label)
    print(tweet_emotion_label)
    print(tweet_hate_label)
    print('--------------------------------------------------------------------------------------------')
    print('\n')
    
def remove_whitespace(text):
    return  " ".join(text.split())

def clean_tweets(tweet_text):
  p.set_options(p.OPT.URL, p.OPT.MENTION)
  clean_tweet_text = p.clean(tweet_text)
  clean_tweet_text = remove_whitespace(clean_tweet_text)
  clean_tweet_text = clean_tweet_text.replace('&amp', "")
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
  convertedstring = ','.join(map(str, wannabestring))
  return(convertedstring)

def tweet_sentiment_analyzer(text):
    
    temp = b_analyzer_sentiment.predict(text)
    bert_sentiment_label = temp.output # output = neg, pos, neu label
    bert_sentiment_score = temp.probas # probas = percentage score
    NEG = round(bert_sentiment_score.get('POS'), 2)
    POS = round(bert_sentiment_score.get('NEG'), 2)
    NEU = round(bert_sentiment_score.get('NEU'), 2)
    score_probability = max(NEG, POS, NEU)
    bert_sentiment_list = [bert_sentiment_label, score_probability]
    
    return(bert_sentiment_list)

def tweet_tokenization(clean_tweet_text):
    
    token = TweetTokenizer()
    temp_tokens = token.tokenize(clean_tweet_text)  
    nltk_tokens = []
    for w in temp_tokens:
         if w not in stop_words:
             if len(w) > 2:
                 nltk_tokens.append(w)
                 
    return(nltk_tokens)

def tweet_emotion_analyzer(text):
    
 temp = b_analyzer_emotion.predict(text)
 label = temp.output
 
 return (label)

def tweet_hate_analyzer(text):
    
     temp = b_analyzer_hate.predict(text)
     temp_label = temp.output
     if len(temp_label) > 2:
          a = temp_label[0]
          b = temp_label[1]
          c = temp_label[2]
          h = (a + " " + b + " " + c)
     elif len(temp_label) == 2:
          a = temp_label[0]
          b = temp_label[1]
          h = (a + " " + b)
          
     elif len(temp_label) == 1:
          h = temp_label[0]
     else:
          h = "None"
     
     return (h)
 
def hydrate_context_annotations(text):
    elist = []
    text = str(text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace(":", ",")
    text = text.replace('"', "").replace("'", "")
    text = text.replace(", ", ",")
    text = text.split(",")
    i = 1
    x = 0
    while i <= len(text):
        if text[x] == 'name':
            elist.append(text[x+1])         
        x = x + 1
        i = i + 1
    temp_str = str(elist)
    temp_str = temp_str.replace("[", "").replace("]", "")
    clist = temp_str.replace("'", "")
    return(clist)

#####################################################################################################################################
#query = '@LaurenArthurMO OR @Dougbeck562 OR @RickBrattin OR @justinbrownmo OR @EricBurlison OR @MikeCierpiot OR @SandyCrawford2 OR @BillEigel OR @SenatorEslinger OR @votegannon OR @DLHoskins OR @lincolnhough OR @Koenig4MO OR @TonyForMissouri OR @KarlaMayMO4 OR @SenAngelaMosley OR @bobondermo OR @gregrazer OR @hrehder OR @RobertsforSTL OR @calebrowden OR @JillSchupp OR @beedubyah1967 OR @BrianWilliamsMO -is:retweet'
#query = 'missouri education -is:retweet'
query = "from:nickbschroer -is:retweet"
project = "fromnickbschroer"
jobtype = "batch"
#query = "moleg -is:retweet"
#####################################################################################################################################

# client = tweepy.Client(
# bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

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

response = client.search_recent_tweets(query=query,tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],media_fields=['duration_ms','height','media_key', 'preview_image_url','promoted_metrics','public_metrics','type,url'],place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],max_results=100)

users = {u['id']: u for u in response.includes['users']}         
for tweet in response.data:  
    #tweet_dict = tweet.data
    #ent_dict = tweet.entities
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        #ent_dict = []
        tweet_dict = tweet.data
        
    if 'public_metrics' in tweet_dict: # TODO #19 public metrics into a function
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
    tweet_reference_soup = tweet.referenced_tweets # TODO #17 referenced tweets into a function
    if tweet_reference_soup is not None:
            tweet_reference = referenced_hydrate(tweet_reference_soup)
            tweet_reference_type = tweet_reference[0] #
            tweet_reference_id = tweet_reference[1] #
    else:
            tweet_reference_type = None
            tweet_reference_id = None
    
    #assign tweet_fields 
    tweet_context_annotations = hydrate_context_annotations(tweet.context_annotations)
    tweet_created_at = tweet.created_at #
    tweet_lang = tweet.lang #
    tweet_reply_settings = tweet.reply_settings #
    tweet_id = tweet.id #
    tweet_source = tweet.source #
    tweet_conversation_id = tweet.conversation_id #
    tweet_text = tweet.text#
    tweet_user = tweet.author_id #
    tweet_in_response_to_user_id = tweet.in_reply_to_user_id #
        
    ######These two functions while separate should be ran together; however instead of creating one function want the option to just get back clean text
    tweet_clean_text = clean_tweets(tweet.text) 
    temp_tweet_sentiment_all = tweet_sentiment_analyzer(tweet_text) #
    tweet_emotion_label = tweet_emotion_analyzer(tweet_clean_text)
    tweet_hate_label = tweet_hate_analyzer(tweet_clean_text) 
    tweet_sentiment_label = temp_tweet_sentiment_all[0]
    tweet_sentiment_score = temp_tweet_sentiment_all[1]
    tweet_sentiment_all = str(temp_tweet_sentiment_all)                  

    #assign user fields to tweet 
    tweet_user_id = user.id            
    temp_tweet_username = user.username
    tweet_username = str(temp_tweet_username) # in some rare cases username was coming back as dict type, converting to string
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

    # TODO #16 Turn this into a function
    # TODO #20 Check to make sure entities is not none
    if tweet.entities:
        ent_dict = tweet.entities
        print(ent_dict)
        if 'mentions' in ent_dict:
                t_mentions = ent_dict.get('mentions')
                tweet_mentions = mention_hydrate(t_mentions) #
                tweet_mentions = makeitastring(tweet_mentions)
                        
        else:
                tweet_mentions = None             
                    
        if 'hashtags' in ent_dict is not None: #is not None needed????
                t_hashtags = ent_dict.get('hashtags')  
                tweet_hashtags = hashtag_hydrate(t_hashtags) #
                tweet_hashtags = makeitastring(tweet_hashtags)
                    
        else:
                tweet_hashtags = None

        if 'annotations' in ent_dict:
                t_annotations = ent_dict.get('annotations')   
                tweet_annotations = annotations_hydrate(t_annotations) #
                tweet_annotations = makeitastring(tweet_annotations)

        else:
                tweet_annotations = None

        if 'urls' in ent_dict:
                t_urls = ent_dict.get('urls')
                tweet_urls = url_hydrate(t_urls) #
                tweet_urls = makeitastring(tweet_urls)
        else:
                tweet_urls = None  
                        
        print_tweet_data() 
     
    #checking for tweet_id since it is primary key
    crsr.execute(
        "SELECT tweet_id, COUNT(*) FROM tweet_all_up WHERE tweet_id = ? GROUP BY tweet_id",
        (tweet_id)
    )
    results = crsr.fetchall()
    row_count = crsr.rowcount

    if row_count == 0: # tweet_id (primary key) does not already exit
        count = crsr.execute("""
        INSERT INTO TWEET_ALL_UP (tweet_id, tweet_created_at, tweet_text, tweet_lang, tweet_source, tweet_reply_settings, tweet_conversation_id, tweet_in_response_to_user_id, tweet_username, tweet_user_tweet_count, tweet_user_description, tweet_user_location, tweet_user_created_at, tweet_user_pinned_tweet, tweet_user_profile_url, tweet_user_verified, tweet_user_listed_count, tweet_user_following_count, tweet_user_followers_count, tweet_like_count, tweet_quote_count, tweet_reply_count, tweet_reference_type, tweet_reference_id, tweet_clean_text, tweet_hashtags, tweet_annotations, tweet_urls, tweet_mentions, tweet_user_id, tweet_context_annotations, query, jobtype, project, tweet_sentiment_label, tweet_sentiment_score, tweet_emotion_label, tweet_hate_label) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        tweet_id, tweet_created_at, tweet_text, tweet_lang, tweet_source, tweet_reply_settings, tweet_conversation_id, tweet_in_response_to_user_id, tweet_username, tweet_user_tweet_count, tweet_user_description, tweet_user_location, tweet_user_created_at, tweet_user_pinned_tweet, tweet_user_profile_url, tweet_user_verified, tweet_user_listed_count, tweet_user_following_count, tweet_user_followers_count, tweet_like_count, tweet_quote_count, tweet_reply_count, tweet_reference_type, tweet_reference_id, tweet_clean_text, tweet_hashtags, tweet_annotations, tweet_urls, tweet_mentions, tweet_user_id, tweet_context_annotations, query, jobtype, project, tweet_sentiment_label, tweet_sentiment_score, tweet_emotion_label, tweet_hate_label).rowcount
        
    crsr.commit()
           
print('Thank you for using Politwit1984.')
cnxn.close() # TODO #11 determine when connection to sql should be closed   
      