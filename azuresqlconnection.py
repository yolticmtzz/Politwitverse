import textwrap
import pyodbc
import dataset
import datetime


def has_value(cursor, table, column, value):
    query = 'SELECT 1 from {} WHERE {} = ? LIMIT 1'.format(table, column)
    return cursor.execute(query, (value,)).fetchone() is not None



driver = '{ODBC Driver 17 for SQL Server}'

server_name = 'twitpoli1984-sqlsrv'
database_name = 'mosenatetweets-db'

server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

tweet_text = "this is tweet text"

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


unid = 1234545645656356

cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
crsr: pyodbc.Cursor = cnxn.cursor()

#insert_sql = "INSERT INTO TWEET_ALL_UP (tweet_created_at ,tweet_id, tweet_text, tweet_lang,tweet_source,tweet_reply_settings,tweet_conversation_id,tweet_in_repsonse_to_user_id,tweet_username,tweet_user_tweet_count,tweet_user_description,tweet_user_created_at,tweet_user_location,tweet_user_pinned_tweet,tweet_user_profile_url,tweet_user_verified,tweet_user_listed_count,tweet_user_following_count,tweet_user_followers_count,tweet_reply_count,tweet_like_count,tweet_quote_count,tweet_reference_type,tweet_reference_id,tweet_clean_text,tweet_sentiment_all,tweet_sentiment_compound,tweet_hashtags,tweet_urls,tweet_annotations,tweet_mentions,tweet_user_id,tweet_context_annotations,tweet_domain_ids,tweet_entity_ids) VALUES"

#checking for tweet_id since it is primary key
crsr.execute(
    "SELECT tweet_id, COUNT(*) FROM tweet_all_up WHERE tweet_id = ? GROUP BY tweet_id",
    (unid)
)
results = crsr.fetchall()
row_count = crsr.rowcount
# print("number of affected rows: {}".format(row_count))
if row_count == 0:
    print("It Does Not Exist")    
    count = crsr.execute("""
    INSERT INTO TWEET_ALL_UP (tweet_text, tweet_lang, tweet_id, tweet_user_listed_count) 
    VALUES (?,?,?,?)""",
    tweet_text, 'jp', 123456789443, 69).rowcount


print('Rows inserted: ' + str(count))
    
crsr.commit()

cnxn.close()



#twitpoli1984-sqlsrv.database.windows.net
#Server=tcp:twitpoli1984-sqlsrv.database.windows.net,1433;Initial Catalog=mosenatetweets-db;Persist Security Info=False;User ID=joewils;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;