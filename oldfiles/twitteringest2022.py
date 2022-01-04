import tweepy
import pandas as pd
import os


client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

df = pd.DataFrame()


# Replace with your own search query
#query = 'from:ShepherdforMO'
query = 'covid'
result = []
user_dict = {}
covidtweets = []
# Get users list from the includes object
#for tweets in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at', 'public_metrics'],
#                                     user_fields=['profile_image_url', 'description', 'location', 'public_metrics'], expansions='author_id', max_results=10).flatten(limit=20):
covidtweets = []
for response in tweepy.Paginator(client.search_recent_tweets, query=query,
                                       tweet_fields=['context_annotations','created_at','public_metrics'],
                                       user_fields=['profile_image_url','description','location','public_metrics'], 
                                       expansions='author_id',
                                       max_results=10).flatten(limit=5):
            covidtweets.append(response)
    

# Loop through each response object
for tweet in covidtweets:
    # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
        for user in response.includes['users']:
             user_dict[user.id] = {'username': user.username, 
                              'followers': user.public_metrics['followers_count'],
                              'tweets': user.public_metrics['tweet_count'],
                              'description': user.description,
                              'location': user.location
                             }
for tweet in response.data:
           # For each tweet, find the author's information
           author_info = user_dict[tweet.author_id]
           # Put all of the information we want to keep in a single dictionary for each tweet
           result.append({'author_id': tweet.author_id, 
                       'username': author_info['username'],
                       'author_followers': author_info['followers'],
                       'author_tweets': author_info['tweets'],
                       'author_description': author_info['description'],
                       'author_location': author_info['location'],
                       'text': tweet.text,
                       'created_at': tweet.created_at,
                       'retweets': tweet.public_metrics['retweet_count'],
                       'replies': tweet.public_metrics['reply_count'],
                       'likes': tweet.public_metrics['like_count'],
                       'quote_count': tweet.public_metrics['quote_count']
                      })
        

# Change this list of dictionaries into a dataframe
df = pd.DataFrame(result)
print(df)
            




# Get users list from the includes object

 #   users = {u["id"]: u for u in tweets.includes['author_ID']}
 #   for tweet in tweets.data:
  #      if users[tweet.author_id]:
   #         user = users[tweet.author_id]
    #        data = {
     #                   'user name': [user.name],
      #                  'user desc': [user.description],
       #                 'user loc' : [user.location],
        #                'tweet text': [tweet.text],
         #               'tweet created' : [tweet.created_at],
          #              'user followers' : user.public_metrics['followers_count'],
           #             'tweet retweet count': tweet.public_metrics["retweet_count"],
            #            'tweet repy count' : tweet.public_metrics["reply_count"],
             #           'user id' : [user.id],
              #          'tweet like count' : tweet.public_metrics['like_count']
                        
  #      }

 #       result.append({     
  #                      'user name' : user.name,  
   #                     'user desc' : user.description,
    #                    'user loc' : user.location,
     #                   'tweet text' : tweet.text,
      #                  'tweet created' : tweet.created_at,
       #                 'user followers' : user.public_metrics['followers_count'],
        #                'tweet retweet count' :  tweet.public_metrics["retweet_count"],
         #               'tweet reply count' : tweet.public_metrics['reply_count'],
          #              'user id' : user.id,
           #             'tweet like count' : tweet.public_metrics['like_count']
        #})

#df = pd.DataFrame(result)

#server = 'twitpoli1984.database.windows.net'
#database = 'mosentatetweets'
#username = 'joewils'
#password = '{Pissyduck113!@}' #-db
#driver= '{ODBC Driver 17 for SQL Server}'

#with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
 #   with conn.cursor() as cursor:
  #      cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
   ##     row = cursor.fetchone()
     #   while row:
      #      print (str(row[0]) + " " + str(row[1]))
      #      row = cursor.fetchone()

#print(df)
#df.to_csv('ingest10.csv')


#loop = asyncio.get_event_loop()
#loop.run_until_complete(run())