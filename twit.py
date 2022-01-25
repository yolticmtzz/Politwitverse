import preprocessor as p
    
def remove_whitespace(text):
    return  " ".join(text.split())

def clean_tweets(tweet_text):
    
  p.set_options(p.OPT.URL, p.OPT.MENTION)
  clean_tweet_text = p.clean(tweet_text)
  clean_tweet_text = remove_whitespace(clean_tweet_text)
  clean_tweet_text = clean_tweet_text.replace('&amp', "")
  
  return(clean_tweet_text)

def makeitastring(wannabestring):
  convertedstring = ','.join(map(str, wannabestring))
  return(convertedstring)

def hydrate_public_metrics(tweet_dict):
      if 'public_metrics' in tweet_dict: 
                public_metrics_dict = (tweet_dict['public_metrics'])
                tweet_retweet_count = public_metrics_dict.get('retweet_count') 
                tweet_like_count = public_metrics_dict.get('like_count') 
                tweet_quote_count = public_metrics_dict.get('quote_count') 
                tweet_reply_count = public_metrics_dict.get('reply_count') 
      return tweet_retweet_count, tweet_like_count, tweet_quote_count, tweet_reply_count
    
    
def hydrate_referenced_tweets(referenced_tweets):
  if referenced_tweets:
      t = makeitastring(referenced_tweets)
      t = t.split('=')
      #t = referenced_tweets.split('=')
      tweet_type = t[2].replace(']', ' ')
      tweet_reference_id = t[1].replace(']', ' ').replace(' type', '')
      referenced_tweets_list = []
      referenced_tweets_list.append(tweet_type)
      referenced_tweets_list.append(tweet_reference_id)
      ref_type = referenced_tweets_list[0]
      ref_id = referenced_tweets_list[1]
  else:
      ref_type = None
      ref_id = None
  return ref_type, ref_id

def annotations_hydrate(entity_list):  
    x = 0 #list index
    i = 1 #list length
    container = []
    entity_length = len(entity_list)
    while i <= entity_length:
        temp_list = entity_list[x]
        t = temp_list.get("type")
        container.append(t)
        n = temp_list.get("normalized_text")                  
        container.append(n)
        i = i + 1
        x = x + 1  
    return container