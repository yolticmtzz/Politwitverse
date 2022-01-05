import tweepy
import autopep8
from humanticfunctions import *
from politwitfunctions import *
import pandas as pd
import http.client
import os
import time
import json
import requests
import sys


import preprocessor as p





query = 'from:potus -is:retweet'

result = []
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
response = client.search_recent_tweets(query=query, max_results=100)
for tweet in response.data:
    result.append(p.clean(tweet.text))
  



USER_ID = "potus"
pers = "sales"
message = result


makeitastring = ''.join(map(str, message))


f = open("humantic_tweets.txt", "w", encoding="utf-8")
f.write(makeitastring)
f.close()

#send_personality_traits(USER_ID, message)

#for x in range(1, 45):
   # time.sleep(1)
   # print('waiting...')


#retrieve_personality_traits(USER_ID, pers)