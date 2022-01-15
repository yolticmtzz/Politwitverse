import textwrap
import pyodbc

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

# select_sql = "SELECT * From [mosenators]"
# crsr.execute(select_sql)
# print(crsr.fetchall())



#insert_sql = "INSERT INTO TWEETS_ALL_UP (tweet_created_at ,tweet_id, tweet_text, tweet_lang,tweet_source,tweet_reply_settings,tweet_conversation_id,tweet_in_repsonse_to_user_id,tweet_username,tweet_user_tweet_count,tweet_user_description,tweet_user_created_at,tweet_user_location,tweet_user_pinned_tweet,tweet_user_profile_url,tweet_user_verified,tweet_user_listed_count,tweet_user_following_count,tweet_user_followers_count,tweet_reply_count,tweet_like_count,tweet_quote_count,tweet_reference_type,tweet_reference_id,tweet_clean_text,tweet_sentiment_all,tweet_sentiment_compound,tweet_hashtags,tweet_urls,tweet_annotations,tweet_mentions,tweet_user_id,tweet_context_annotations,tweet_domain_ids,tweet_entity_ids) VALUES"

#insert_sql = "INSERT INTO [tweets_all_up] (Senator, District, Party, Followers, UserDescription, StatusCount, Location) VALUES (?, ?, ?, ?, ?, ?, ?)"

# insert_sql = "INSERT INTO TWEETS_ALL_UP (tweet_created_at ,tweet_id, tweet_text) VALUES ()
# records = [
#     ('2022-01-11 21:44:06+00:00', 1466258632627130373, 'tweet text')
#     ]
    
crsr.execute("INSERT INTO TWEETS_ALL_UP (tweet_id, tweet_text) VALUES (%s, %s);", (1234567, "tweettext150"))
#print("Inserted",cursor.rowcount,"row(s) of data.")



#crsr.executemany(insert_sql, records)
#crsr.commit()

cnxn.close()



#twitpoli1984-sqlsrv.database.windows.net
#Server=tcp:twitpoli1984-sqlsrv.database.windows.net,1433;Initial Catalog=mosenatetweets-db;Persist Security Info=False;User ID=joewils;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;