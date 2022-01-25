import tweepy
from pysentimiento import create_analyzer
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import spacy

b_analyzer_sentiment = create_analyzer(task="sentiment", lang="en")
b_analyzer_emotion = create_analyzer(task="emotion", lang="en")
b_analyzer_hate = create_analyzer(task="hate_speech", lang="en")
v_analyzer_sentiment = SentimentIntensityAnalyzer()
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAAQ6Wu3fVaVsdg4PHyN7ktSku8u8g%3DMWmLEo5o3YPP0HsKRrX5S1UcKAnemvF2UVPG5Sp6S2qXRFNB9j')
TweetTokenizer()
stop_words = set(stopwords.words('english'))
nlp = spacy.load('en_core_web_sm')

def tweet_sentiment_analyzer(text):
    
    temp = b_analyzer_sentiment.predict(text)
    bert_sentiment_label = temp.output # output = neg, pos, neu label
    bert_sentiment_score = temp.probas # probas = percentage score
    NEG = round(bert_sentiment_score.get('POS'), 2)
    POS = round(bert_sentiment_score.get('NEG'), 2)
    NEU = round(bert_sentiment_score.get('NEU'), 2)
    score_probability = max(NEG, POS, NEU)
    # bert_sentiment_list = [bert_sentiment_label, score_probability]
    
    return bert_sentiment_label, score_probability

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



