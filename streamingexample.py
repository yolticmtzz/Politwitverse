import tweepy
import os
import config

# Subclass Stream to print IDs of Tweets received
class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)

# Initialize instance of the subclass
printer = IDPrinter(
  config.consumer_key, config.consumer_secret,
  config.access_token, config.access_token_secret
)

# Filter realtime Tweets by keyword
printer.filter(track=["Twitter"])

