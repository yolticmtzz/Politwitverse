import tweepy
from humanticfunctions import *
from politwitfunctions import *
import pandas as pd
import http.client
import os
import time
import json
import requests

query = 'from:kingofjuco -is:retweet'

result = []
#client = tweepy.Client(
#bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
#response = client.search_recent_tweets(query=query, max_results=100)
#for tweet in response.data:
#    result.append(tweet.text)

USER_ID = "stltoday"
pers = "sales"
#message = result
message = "Rep. Justin Hill said on his Facebook page that in Florida he would build his consulting business and work on advocacy. He said he had been “involved in state policy development at the national level for quite some time” and realized “the best way to continue these efforts over the long term is to step down from public office and continue my efforts within the private sector. Hill has stoked controversy in the past, skipping his own swearing-in last year to attend the Jan. 6 rally in Washington, D.C. that preceded the attack on the U.S. Capitol by supporters of then-outgoing President Donald Trump. His departure, along with the expected resignation of Rep. Aaron Griesheimer of Washington, will take Republicans below the two-thirds majority necessary in the House to immediately enact a new map of the state’s eight congressional districts, increasing reliance on Democratic votes."

#makeitastring = ''.join(map(str, message))
#print(makeitastring)

f = open("humantic_tweets.txt", "w")
f.write(message)
f.close()

send_personality_traits(USER_ID, message)

for x in range(1, 45):
    time.sleep(1)
    print('waiting...')


retrieve_personality_traits(USER_ID, pers)