# created_at : The time the status was posted.
# id : The ID of the status.
# id_str : The ID of the status as a string.
# text : The text of the status.
# entities : The parsed entities of the status such as hashtags, URLs etc.
# source : The source of the status.
# source_url : The URL of the source of the status.
# in_reply_to_status_id : The ID of the status being replied to.
# in_reply_to_status_id_str : The ID of the status being replied to in as a string.
# in_reply_to_user_id : The ID of the user being replied to.
# in_reply_to_user_id_str : The ID of the user being replied to as a string.
# in_reply_to_screen_name : The screen name of the user being replied to
# user : The User object of the poster of the status.
# geo : The geo object of the status.
# coordinates : The coordinates of the status.
# place : The place of the status.
# contributors : The contributors of the status.
# is_quote_status : Indicates whether the status is a quoted status or not.
# retweet_count : The number of retweets of the status.
# favorite_count : The number of likes of the status.
# favorited : Indicates whether the status has been favourited by the authenticated user or not.
# retweeted : Indicates whether the status has been retweeted by the authenticated user or not.
# possibly_sensitive : Indicates whether the status is sensitive or not.
# lang : The language of the status. 

import tweepy
import pandas as pd
import csv

API_KEY = "anvCaAUUuYqG3xLR7dNAzR0dr"
API_SECRET_KEY = "ULtEkEdycJzC08cyebSg1ExdOVgCg5pUG0qtLPnLta24ClNDqr"
ACCESS_TOKEN = "1469761271709028359-FrJt9sku3toFacDx1tdvmSPc273pKf"
ACCESS_TOKEN_SECRET = "mlblwNEQ21A6IrmC4boX42Rctpq0WLNMfTsoOSmOwPrAa"

# tweet_column_names = ["tweet_id", "tweet_text", "tweet_entities", "tweet_source", "tweet_source_url", "tweet_in_reply_to_status_id",        "tweet_in_reply_to_user_id", "tweet_in_reply_to_screen_name", "tweet_username,", "tweet_user", "tweet_geo", "tweet_coordinates", "tweet_place", "tweet_coordinates", "tweet_is_quote_status", "tweet_retweet_count", "tweet_favorited_count", "tweet_favorited", "tweet_retweted", "tweet_lang", "tweet_created_at"]

#df = pd.DataFrame()
#df = pd.DataFrame(columns = tweet_column_names)
        
        
stream = tweepy.Stream(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

class IDPrinter(tweepy.Stream):


    def on_status(self, status):
      
        # tweet_column_names = ["tweet_id", "tweet_text", "tweet_entities", "tweet_source", "tweet_source_url", "tweet_in_reply_to_status_id",        "tweet_in_reply_to_user_id", "tweet_in_reply_to_screen_name", "tweet_username,", "tweet_user", "tweet_geo", "tweet_coordinates", "tweet_place", "tweet_coordinates", "tweet_is_quote_status", "tweet_retweet_count", "tweet_favorited_count", "tweet_favorited", "tweet_retweeted", "tweet_lang", "tweet_created_at"]
        
        #fields = [tweet_id, tweet_text, tweet_entities, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_user_id, tweet_in_reply_to_screen_name, tweet_username,, tweet_user, tweet_geo, tweet_coordinates, tweet_place, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_favorited_count, tweet_favorited, tweet_retweted, tweet_lang, tweet_created_at]

        # df = pd.DataFrame()
        # df = pd.DataFrame(columns = tweet_column_names)
        
        tweet_id = status.id
        tweet_text = status.text
        tweet_entities = status.entities
        tweet_source = status.source
        tweet_source_url = status.source_url
        tweet_in_reply_to_status_id = status.in_reply_to_status_id
        tweet_in_reply_to_user_id = status.in_reply_to_user_id
        tweet_in_reply_to_screen_name = status.in_reply_to_screen_name
        tweet_username = status.user.screen_name
        tweet_user = status.user
        tweet_geo = status.geo
        tweet_coordinates = status.coordinates
        tweet_place = status.place
        tweet_coordinates = status.coordinates
        tweet_is_quote_status = status.is_quote_status
        tweet_retweet_count = status.retweet_count
        tweet_favorited_count = status.favorite_count
        tweet_favorited = status.favorited
        tweet_retweeted = status.retweeted
        tweet_lang = status.lang
        tweet_created_at = status.created_at
        print(tweet_username)
        print(tweet_text)
        
        # fields_data = ([tweet_id, tweet_text, tweet_entities, tweet_source, tweet_source_url, tweet_in_reply_to_status_id, tweet_in_reply_to_user_id, tweet_in_reply_to_screen_name, tweet_username,, tweet_user, tweet_geo, tweet_coordinates, tweet_place, tweet_coordinates, tweet_is_quote_status, tweet_retweet_count, tweet_favorited_count, tweet_favorited, tweet_retweted, tweet_lang, tweet_created_at])

                
        # with open('OutputStreaming.txt', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(fields)
        
        # new_row = {"tweet_id":tweet_id, "tweet_text":tweet_text, "tweet_entities":tweet_entities, "tweet_source":tweet_source, "tweet_source_url":tweet_source_url, "tweet_in_reply_to_status_id":tweet_in_reply_to_status_id, "tweet_in_reply_to_user_id":tweet_in_reply_to_user_id, "tweet_in_reply_to_screen_name":tweet_in_reply_to_screen_name, "tweet_username":tweet_username, "tweet_user":tweet_user, "tweet_geo":tweet_geo, "tweet_coordinates":tweet_coordinates, "tweet_place":tweet_place, "tweet_coordinates":tweet_coordinates, "tweet_is_quote_status":tweet_is_quote_status, "tweet_retweet_count":tweet_retweet_count, "tweet_favorited_count":tweet_favorited_count, "tweet_favorited":tweet_favorited, "tweet_retweeted":tweet_retweeted, "tweet_lang":tweet_lang, "tweet_created_at":tweet_created_at}
        
        #df = df.append(new_row, ignore_index=True)
        

        # df.to_csv('streaming2.csv', mode='a')
        
        #del df

printer = IDPrinter(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# with open('OutputStreaming.txt', 'w') as f:
# writer = csv.writer(f)
# writer.writerow(["tweet_id", "tweet_text", "tweet_entities", "tweet_source", "tweet_source_url", "tweet_in_reply_to_status_id",        "tweet_in_reply_to_user_id", "tweet_in_reply_to_screen_name", "tweet_username,", "tweet_user", "tweet_geo", "tweet_coordinates", "tweet_place", "tweet_coordinates", "tweet_is_quote_status", "tweet_retweet_count", "tweet_favorited_count", "tweet_favorited", "tweet_retweted", "tweet_lang", "tweet_created_at"])


printer.filter(track=['hostage'],languages=["en"])




#################################################################################################
