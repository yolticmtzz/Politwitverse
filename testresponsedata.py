import tweepy
import re

def makeitastring(wannabestring):
  convertedstring = ''.join(map(str, wannabestring))
  return(convertedstring)

query = 'covid'
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

response = client.search_recent_tweets(query=query, tweet_fields=['context_annotations'], max_results=10)

#response = client.search_recent_tweets(query=query,
#                                       tweet_fields=['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo,id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
 #                                       user_fields=['created_at','description','entities','id','location,name','pinned_tweet_id','profile_image_url','protected,public_metrics','url','username','verified','withheld'],
  #                                      expansions=['attachments.poll_ids','attachments.media_keys','author_id','geo.place_id','in_reply_to_user_id','referenced_tweets.id','entities.mentions.username','referenced_tweets.id.author_id'],
   #                                     media_fields=['duration_ms','height','media_key','preview_image_url','promoted_metrics','public_metrics','type,url'],
    #                                    place_fields=['contained_within,country','country_code','full_name','geo,id','name','place_type'],
     #                                   poll_fields=['duration_minutes','end_datetime','id,options','voting_status'], 
      #                                  max_results=10)


tweet_data = {'annotations': [{'start': 138, 'end': 148, 'probability': 0.7903, 'type': 'Organization', 'normalized_text': 'ABC 17 News'}],
'urls': [{'start': 156, 'end': 179, 'url': 'https://t.co/15WquQszJ8', 'expanded_url': 'https://abc17news.com/news/coronavirus/2022/01/10/mid-missouri-schools-move-ahead-with-in-person-learning-as-coronavirus-surge-sets-records/', 'display_url': 'abc17news.com/news/coronavir…', 'images': [{'url': 'https://pbs.twimg.com/news_img/1480683946107150336/HFUu5KAB?format=jpg&name=orig', 'width': 1892, 'height': 980}, {'url': 'https://pbs.twimg.com/news_img/1480683946107150336/HFUu5KAB?format=jpg&name=150x150', 'width': 150, 'height': 150}], 'status': 200, 'title': 'Mid-Missouri schools move ahead with in-person learning as coronavirus surge sets records - ABC17NEWS', 'description': 'School is back in session for districts around Mid-Missouri, but the return to classrooms has coincided with a meteoric rise in new coronavirus infections, causing at least one area school to hold remote classes and creating worries among some parents.', 'unwound_url': 'https://abc17news.com/news/coronavirus/2022/01/10/mid-missouri-schools-move-ahead-with-in-person-learning-as-coronavirus-surge-sets-records/'}]}
#tweet_dict = tweet_data
#print(tweet_dict)
#print(tweet_dict.keys())


for tweet in response.data:
    referenced_tweets = []
    #print(tweet.context_annotations)
    referenced_tweets = tweet.context_annotations
    print(len(referenced_tweets))
    print('\n')
    if len(referenced_tweets) > 1:
        t = referenced_tweets[0]
        print(type(t))
        #tweet_type = t.replace("']{{}:", '')
        tt = {}
        tt = t
        print(tt.keys())
        print(type(tt))
        print(tt.get('entity'))
        print(tt.get('domain'))
        print(tt)
    

    #print(tweet_type)
#tweet_reference_id = t[1].replace(']', ' ').replace(' type', '')
#referenced_tweets_list = []
#referenced_tweets_list.append(tweet_type)
#referenced_tweets_list.append(tweet_reference_id)