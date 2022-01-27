from sqlalchemy import null
import tweepy
import textwrap
import pyodbc
import preprocessor as p
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pysentimiento import create_analyzer
import spacy

b_analyzer_sentiment = create_analyzer(task="sentiment", lang="en")
b_analyzer_emotion = create_analyzer(task="emotion", lang="en")
b_analyzer_hate_speech = create_analyzer(task="hate_speech", lang="en")
v_analyzer_sentiment = SentimentIntensityAnalyzer()
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAAQ6Wu3fVaVsdg4PHyN7ktSku8u8g%3DMWmLEo5o3YPP0HsKRrX5S1UcKAnemvF2UVPG5Sp6S2qXRFNB9j')

TweetTokenizer()
stop_words = set(stopwords.words('english'))
nlp = spacy.load('en_core_web_sm')

API_KEY = "anvCaAUUuYqG3xLR7dNAzR0dr"
API_SECRET_KEY = "ULtEkEdycJzC08cyebSg1ExdOVgCg5pUG0qtLPnLta24ClNDqr"
ACCESS_TOKEN = "1469761271709028359-FrJt9sku3toFacDx1tdvmSPc273pKf"
ACCESS_TOKEN_SECRET = "mlblwNEQ21A6IrmC4boX42Rctpq0WLNMfTsoOSmOwPrAa"      
        
stream = tweepy.Stream(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# TODO #10 must have better error detection and not fail on an exception
class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        if hasattr(status, "retweeted_status"):  # Check if Retweet
            try:
                print(status.retweeted_status.extended_tweet["full_text"]) ############################################ console output
                tweet_text = status.retweeted_status.extended_tweet["full_text"]
                tweet_retweeted = "TRUE"
                print("retweeted") ############################################ console output
            except AttributeError:
                print(status.retweeted_status.text) ############################################ console output
                tweet_text = status.retweeted_status.text
                tweet_retweeted = "TRUE"
                print("retweeted") ############################################ console output
        else:
            try:
                print(status.extended_tweet["full_text"]) ############################################ console output
                tweet_text = status.extended_tweet["full_text"]
                tweet_retweeted = "FALSE"
                print("Original Tweet")
            except AttributeError:
                print(status.text) ############################################ console output
                tweet_text = status.text
                tweet_retweeted = "FALSE"
                print("Original Tweet") ############################################ console output
        
        ###########################################################################################################################
        # query = '''education moleg', 'missouri education', 'missouri mandate', 'missouri schools', 'missouri teachers', 'missouri students', 'missouri dese', 'missouri public schools', 'missouri charter schools', 'missouri private schools', 'missouri school boards', 'misssouri school covid', 'missouri school masks lang:en'''
        # project = 'realtime education analysis'
        # jobtype = "stream"
        
        query = 'moleg'
        project = 'molegmaskeducation'
        jobtype = "stream"
        
        # query = 'missouri covid lang:en'
        # project = 'missouri covid test data'
        # jobtype = "stream"
        
        # query = 'covid lang:en'
        # project = 'covid test data'
        # jobtype = "stream"
        ###########################################################################################################################
        
        if tweet_retweeted == "FALSE":  #only insert into database if it isn't a retweet
        
                tweet_id = status.id
                
                ent_dict = status.entities

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

                # TODO #13 parse data out of place object
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
                tweet_in_reply_to_screen_name = status.in_reply_to_screen_name
                temp_tweet_username = status.user.screen_name  
                tweet_username = str(temp_tweet_username)  # in some rare cases a username comes back as a dict type so converting to string         
                #tweet_user = status.user
                tweet_geo = status.geo
                tweet_coordinates = status.coordinates
                #tweet_place = status.place
                tweet_is_quote_status = status.is_quote_status
                tweet_retweet_count = status.retweet_count
                tweet_like_count = status.favorite_count
                tweet_favorited = status.favorited
                tweet_lang = status.lang
                tweet_created_at = status.created_at
                tweet_user_description = status.user.description
                tweet_clean_text = clean_tweets(tweet_text) #
                tweet_sentiment_all = tweet_sentiment_analyzer(tweet_clean_text) #
                tweet_sentiment_label = tweet_sentiment_all[0] # label is first item in list - pos, neg, neu
                tweet_sentiment_score = tweet_sentiment_all[1] # score is second item in list  - decimal
                tweet_user_verified = status.user.verified
                tweet_user_followers_count = status.user.followers_count
                tweet_user_listed_count = status.user.listed_count
                #place_field = place.id                
                tweet_user_location = status.user.location
                tweet_user_id = status.user.id                
                tweet_in_response_to_user_id = status.in_reply_to_user_id                
                #tweet_user_url = status.user.url #doublecheck
                #tweet_in_response_to_user_id = status.in_reply_to_user_id                
                tweet_user_created_at = status.user.created_at
                tweet_user_like_count = status.user.favourites_count 
                tweet_user_following_count = status.user.friends_count # this may be status.user.following
                tweet_user_profile_url = status.user.url              
                tweet_user_tweet_count = status.user.statuses_count
                user_influence_score = influence_score(tweet_user_verified, tweet_user_tweet_count, tweet_user_followers_count, tweet_user_listed_count, tweet_user_like_count)
                print(tweet_username) ############################################ console output
                print(user_influence_score) ############################################ console output
                print('\n') ############################################ console output
                print(tweet_sentiment_all)
                print(status.contributors)
                print('-------------------------------------------------------------------------------------------')

                # checking for tweet_id since it is primary key
                crsr.execute(
                    "SELECT tweet_id, COUNT(*) FROM tweet_all_up WHERE tweet_id = ? GROUP BY tweet_id",
                    (tweet_id)
                )
                results = crsr.fetchall()
                row_count = crsr.rowcount
                
                if row_count == 0:
                    # print("It Does Not Exist") # output to console that primary key doesn't exist   
                    count = crsr.execute("""
                    INSERT INTO TWEET_ALL_UP (tweet_id, tweet_text, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_screen_name, tweet_username, tweet_geo, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_like_count, tweet_favorited, tweet_retweeted, tweet_lang, tweet_created_at, query, project, tweet_mentions, tweet_hashtags, tweet_urls, tweet_user_description, jobtype, tweet_clean_text, tweet_user_verified, tweet_user_followers_count, tweet_user_listed_count, tweet_user_location, tweet_user_id, tweet_user_created_at, tweet_user_like_count, tweet_user_following_count, tweet_user_profile_url, tweet_user_tweet_count, tweet_in_response_to_user_id, user_influence_score, tweet_sentiment_label, tweet_sentiment_score) 
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    tweet_id, tweet_text, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_screen_name, tweet_username, tweet_geo, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_like_count, tweet_favorited, tweet_retweeted, tweet_lang, tweet_created_at, query, project, tweet_mentions, tweet_hashtags, tweet_urls, tweet_user_description, jobtype, tweet_clean_text, tweet_user_verified, tweet_user_followers_count, tweet_user_listed_count, tweet_user_location, tweet_user_id, tweet_user_created_at, tweet_user_like_count, tweet_user_following_count, tweet_user_profile_url, tweet_user_tweet_count, tweet_in_response_to_user_id, user_influence_score, tweet_sentiment_label, tweet_sentiment_score).rowcount

                    #removing tweet_entities, tweet_user (can pull individual attributes), tweet_in_response_to_user_id (dict can't be inserted into SQL), tweet_place
                    
                crsr.commit()
                #cnxn.close() # TODO #11 determine when connection to sql should be closed 


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

## TODO #9 need to figure out how to get place data out of the object as it isn't a dictionary
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

# TODO #12 remove &amp from tweet text when it is being cleaned
def clean_tweets(tweet_text):
  p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
  clean_tweet_text = p.clean(tweet_text)
  clean_tweet_text = clean_tweet_text.replace("&amp", "") 
  clean_tweeet_text = remove_whitespace(clean_tweet_text)
  return(clean_tweet_text)

#creates a dictionary of positive score, neutral score, negativie score or compound score. Here it is 
def tweet_sentiment_analyzer(clean_text):

  sentiment_scores = []
  sentiment_scores = analyzer.polarity_scores(clean_text)
  return(sentiment_scores)

def influence_score(tweet_user_verified, tweet_user_tweet_count, tweet_user_followers_count, tweet_user_listed_count, tweet_user_like_count):
    score = 0
    if tweet_user_verified:
        score = score + 4000
    if tweet_user_tweet_count > 0:
        score = score + (tweet_user_tweet_count * .05)
    if tweet_user_followers_count > 0:
        score = score + (tweet_user_followers_count * .2)
    if tweet_user_listed_count > 0:
        score = score + (tweet_user_listed_count * 200)
    if tweet_user_like_count > 0:
        temp_user_like_score = (tweet_user_like_count * .05)
        if temp_user_like_score > 10000:
            score = score + 10000
        else:
            score = score + temp_user_like_score
    temp_score = (score / 10000) 
    influence = round(temp_score, 2)       
    return(influence)

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
    """tokenizes a sentence

    Args:
        clean_tweet_text ([str]): [tweet that has been sent through a function that removes unnecessary whitespace, characters, etc.]
    """
    token = TweetTokenizer()
    temp_tokens = token.tokenize(clean_tweet_text)  
    nltk_tokens = []
    for w in temp_tokens:
         if w not in stop_words:
             if len(w) > 2:
                 nltk_tokens.append(w)
                 
    return(nltk_tokens)

ent_dict = []
analyzer = SentimentIntensityAnalyzer()

################################################################################################################################
printer.filter(track=['moleg', 'missouri covid', 'missouri education', 'missouri schools', 'missouri house', 'missouri senate', 'mogov'],languages=["en"])
#printer.filter(track=['education moleg', 'missouri education', 'missouri mandate', 'missouri schools', 'missouri teachers', 'missouri students', 'missouri dese', 'missouri public schools', 'missouri charter schools', 'missouri private schools', 'missouri school boards', 'misssouri school covid', 'missouri school masks', 'SB657', 'HB1474', 'HB1995', 'missouri defund'],languages=["en"])
#printer.filter(track=['Arizona Cardinals', 'Los Angeles Rams', 'LA Rams', 'Cardinals football', "football"],languages=["en"])
#printer.filter(follow=['979769447656382464'], languages=["en"])
################################################################################################################################

