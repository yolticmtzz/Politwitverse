import tweepy
from humanticfunctions import *
from politwitfunctions import *
import pandas as pd
import http.client
import os
import time
import json


query = 'from:repthomasmassie -is:retweet'

result = []



sun = 'repthomasmassie'
sp = 'https://twitter.com/repthomasmassie'
HID = 'abcdefg12345'
pers = 'sales'

send_personality_traits(sun, sp, HID, result)
for x in range(1, 45):
    time.sleep(1)
    print('waiting...')
retrieve_personality_traits(sun, sp, HID, result, pers)




        




