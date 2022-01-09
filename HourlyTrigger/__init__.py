import tweepy
import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

query = 'Missouri education'

client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')
response = client.search_recent_tweets(query=query,
                                       tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
                                       user_fields=['created_at','description','entities,id','location,name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
                                       expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],
                                       media_fields=['duration_ms','height','media_key','preview_image_url','promoted_metrics','public_metrics','type,url'],
                                       place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],
                                       poll_fields=['duration_minutes','end_datetime','id,options','voting_status'], 
                                       max_results=10)

response = client.get_recent_tweets_count(query=query, granularity="day")
print(response)
