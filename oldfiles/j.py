import tweepy
import json
import pandas as pd
import json
import sys

import pyodbc

driver = '{ODBC Driver 17 for SQL Server}'
server = 'twitpoli1984-sqlsrv'
database = 'mosenatetweets-db'
username = 'joewils'
password = 'Pissyduck113!@'

#Driver={ODBC Driver 13 for SQL Server};Server=tcp:twitpoli1984-sqlsrv.database.windows.net,1433;Database=mosenatetweets-db;Uid=joewils;Pwd=Pissyduck113!@;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;


with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()


# query = 'missouri education -is:retweet'
# client = tweepy.Client(
# bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
# tweets = client.search_recent_tweets(query=query, max_results=10)



# # Save data as dictionary
# tweets_dict = tweets._json() 

# # Extract "data" value from dictionary
# tweets_data = tweets_dict['data'] 

# # Transform to pandas Dataframe
# df = pd.json_normalize(tweets_data) 

# print(df)
