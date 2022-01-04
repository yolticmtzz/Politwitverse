import tweepy
from humanticfunctions import *
from politwitfunctions import *
import pandas as pd
import http.client
import os
import time
import json
import requests

query = 'from:baueroutage -is:retweet'

result = []
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
response = client.search_recent_tweets(query=query, max_results=100)
for tweet in response.data:
    result.append(tweet.text)

USER_ID = "https://twitter.com/baueroutage"
message = result
print(USER_ID)
print(message)

send_personality_traits(USER_ID, message)

for x in range(1, 45):
    time.sleep(1)
    print('waiting...')


retrieve_personality_traits(sun, sp, HID, result, pers)