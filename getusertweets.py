import tweepy
import time
import os
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg'
consumer_key = 'M4fMgH6O8YCEK2WsNdwrU8uva'
consumer_secret =  'TUMYv7JLjTT0se5Y4Xv7n3zZjgv4FivIjsXzazpPdxTCVN63NR'
access_token = '1469761271709028359-m8mLVjn0MD2Tf9LOuv6gaOe8ke1DT1'
access_token_secret = 'UWFeA678yMNZxJNmICaNBQEPlGtooBeNA83zbcJwiEip0'



# Authenticate to Twitter
client = tweepy.Client(bearer_token)

#Set keyword search - query can be up to 512


#sent query to be searched; initialize tweet variable
#for response in tweepy.Paginator(client.get_users_following, id=1021897086793658368, max_results=10, limit=5):
 #   print(response.meta)
username = "ShepherdForMO"
response = client.get_user(username=username)
query = "from:ShepherdForMO"

id = 3434654170

tweets = client.search_recent_tweets(query=query,max_results=10,tweet_fields=["author_id","created_at","public_metrics","source"],user_fields=["username","name","created_at","description"])
users = {u["id"]: u for u in tweets.includes['users']}
user = users[tweet.author_id]  
for tweet in tweets.data:
        print(tweet.text)
        print(tweet.author_id)
        print(tweet.username)

                  
users = {u["id"]: u for u in tweets.includes['users']}