import tweepy 
import shlex

def hydrate_context_annotations(text):
    elist = []
    text = str(text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace(":", ",")
    text = text.replace('"', "").replace("'", "")
    text = text.replace(", ", ",")
    text = text.split(",")
    i = 1
    x = 0
    while i <= len(text):
        if text[x] == 'name':
            elist.append(text[x+1])         
        x = x + 1
        i = i + 1
    temp_str = str(elist)
    temp_str = temp_str.replace("[", "").replace("]", "")
    clist = temp_str.replace("'", "")
    return(clist)



client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAAQ6Wu3fVaVsdg4PHyN7ktSku8u8g%3DMWmLEo5o3YPP0HsKRrX5S1UcKAnemvF2UVPG5Sp6S2qXRFNB9j')

query = "missouri covid -is:retweet lang:en"
# response = client.search_recent_tweets(query=query, tweet_fields=['author_id'], user_fields=['created_at', 'name'],
#                               max_results=10)

response = client.search_recent_tweets(query=query,tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],user_fields=['created_at','description','entities,id','location','name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],media_fields=['duration_ms','height','media_key', 'preview_image_url','promoted_metrics','public_metrics','type,url'],place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],max_results=10) 



for tweet in response.data: 
    print(tweet.text)


