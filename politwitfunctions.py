import tweepy
import pandas as pd
import os

def strip_just_tweets(sentences):
  dataset = [sentences]
  for tweet in dataset:
     dataset.append[tweet.text]
  return dataset

  

def get_user_personality_tweets(personality_tweets):

    result = []
    # Loop through each response object
     
    for tweet in response.data:
        #print(tweet.text)
        #author_info = user_dict[tweet.author_id]
        #text_sentiment = textblob(tweet.text)
        #Put all of the information we want to keep in a single dictionary for each tweet
        result.append({tweet.text})
        df = pd.DataFrame(result)
        #print(df)



# placeholder for user portion of tweets and user follower functions
#id = '3434654170'
#myid id = '1021897086793658368'
#user_results1 = []
#response = client.get_users_followers(id=id,
#                                 max_results=10)
#for user in response.data:
##   print(user.username)
    #print(user.id)

#result1 = []
#user_dict1 = {}
# Loop through each response object
#for user in response.data:
    # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
    #user_dict1[user.id] = {'username': user.username, 
  #                            'id': user.id}
    #result1.append({    'username': user.username,
   #                    'userID' : user.id
  #                    })

# Change this list of dictionaries into a dataframe
#df1 = pd.DataFrame(result)
#print(df1)



# Replace user ID
#id = '3434654170'
##myid id = '1021897086793658368'
#user_results = []
#response = client.get_users_followers(id=id,
 #                                max_results=10)
#for data in response:
 #   print(user.username)





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