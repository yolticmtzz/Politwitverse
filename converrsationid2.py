import tweepy
import pyodbc
import textwrap

# functions used to streamline getting data out of tweet and user payloads
from twit import *
import time
import os
import config

bearer_token = config.bearer_token


client = tweepy.Client(bearer_token=bearer_token)
client2 = tweepy.Client(bearer_token=bearer_token)

query = "conversation_id:1487526628674748420"

id = 1487833785559306250


response = client.search_recent_tweets(
    query=query,
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "entities",
        "geo,id",
        "in_reply_to_user_id",
        "lang",
        "possibly_sensitive",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities,id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected,public_metrics",
        "url",
        "username",
        "verified",
        "withheld",
    ],
    expansions=[
        "attachments.poll_ids",
        "attachments.media_keys",
        "author_id",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "entities.mentions.username",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "duration_ms",
        "height",
        "media_key",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type,url",
    ],
    place_fields=[
        "contained_within,country",
        "country_code",
        "full_name",
        "geo,id",
        "name",
        "place_type",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    max_results=100,
)

tweets = response.data

response = client2.get_tweet(id, tweet_fields=["created_at"])
mytweet = response.data

for tweet in tweets:
    print(mytweet.text)
    print(tweet.id)
