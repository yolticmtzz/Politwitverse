import tweepy
from collections import defaultdict
import time
import json
import re
import pickle
import ast


def def_value():
    return "Not Present"

def entities_strip(entities_soup):
#assuming username stays at index [2] when Twitter passes back entities data
            print('entities soup')
            #print(entities_soup)
            temp_str = (entities_soup[0])
            txt = makieitastring(temp_str)
            #txt2 = txt.strip('}')
            temp_list = txt2.split(",")
            #print('temp list')
            #cleprint(temp_list)
            tusername = temp_list[2]
            username = tusername.split(':')[1].lstrip().split(' ')[0]
            return(username)

def makeitastring(wannabestring):
  convertedstring = ''.join(map(str, wannabestring))
  return(convertedstring)

def Convert(lst):
    op = { i : lst[i] for i in range(0, len(lst) ) }
    return op

query = 'covid'
client = tweepy.Client(
bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

response = client.search_recent_tweets(query=query, tweet_fields=['entities'], max_results=100)


ent_dict = {}
f = open("myfile.txt", "a")  # write mode

t_mentions = []
t_urls = []
t_annotations = []
t_hashtags = []
txt2 = '[]()'
#################################################see if converting text.entities to json is more efficient###############################
a = 0
while a < 100:
    for tweet in response.data: 
        annotations = None
        urls = None
        mentions = None
        hashtags = None
        id = tweet.id
        ent_dict = tweet.entities
        #print('#############################################################################')
        #print(ent_dict)
        #print(len(ent_dict))
        
        #print(tweet.entities)
        print(tweet.id)
        #print(a)
        if 'hashtags' in ent_dict:
            print("hashtags exists")
            #print(hashtags)
            t_hashtags = ent_dict.get('hashtags')
            #print(ent_dict)
            

        else:
            print("hashtags does not exist")

        if 'mentions' in ent_dict:
            print("mentions exists")
        #    t_mentions = ent_dict.get('mentions')
        #    username = entities_strip(t_mentions)
            #temp_str = str(t_mentions[0])
            #tmp_list = []
            #txt = temp_str.strip('{}')
            #temp_list = txt.split(",")
            #print(t_mentions)
            #print(temp_list[2])
            #tusername = temp_list[2]
            #username = tusername.split(':')[1].lstrip().split(' ')[0]
        #    print(username)
            

        else:
            print("mentions does not exist")

        if 'annotations' in ent_dict:
            annotations_dict = defaultdict(def_value)
            print("annotations exists")
            t_annotations = ent_dict.get('annotations')
            print(len(t_annotations))
            s_annotations = makeitastring(t_annotations)
            y = str(s_annotations)
            annotations_length = len(t_annotations)     
            print(annotations_length)
            x=0
            i=1
            while i <= annotations_length:
                print(t_annotations[x])
                #txt = makieitastring(temp_str)
                #txt2 = txt.strip('}')
                #temp_list = txt2.split(",")
                #print('temp list')
                #cleprint(temp_list)
                #tusername = temp_list[2]
                #username = tusername.split(':')[1].lstrip().split(' ')[0]

                jj_annotations_indexed = t_annotations[x]
                print(jj)
                print(type(jj))
                
                i = i + 1
                x = x + 1


                

            #yy = y.replace("'", '"')
            #annotations_dict = ast.literal_eval(y)
            #print(list_yy)
            #result = json.loads(yy)


            #annotations_dict = dict(list_yy.split(":"))
            #print(annotations_dict)




            

            #dic = dict(subString.split("=") for subString in str.split(";"))
            #print(annotations_list)


        else:
            print("annotations does not exist")

        if 'urls' in ent_dict:
            print("urls exists")
            print(urls)
            t_hashtags = ent_dict.get('urls')

        else:
            print("urls does not exist")
        a = a + 1

      
   

    #ent_dict.get(hashtags)

    #if mentions is not None or 'empty':
    #ent_dict[tweet.id] +- mentions

   # urls = tweet.entities.get('urls', 'empty')
    #if urls is not None or 'empty':
    #ent_dict[tweet.id] = urls

   #annotations = tweet.entities.get('annotations', 'empty')
   # if annotations is not None or 'empty':
#ent_dict[tweet.id] = annotations

    #hashtags = tweet.entities.get('hashtags', 'empty')
    #if hashtags is not None or 'empty':
    #ent_dict[tweet.id] = hashtags

#print(ent_dict)
    
    #print(tweet.text)
    #print(id)
    #print(tweet.entities.get('urls'))
    #print(tweet.entities)
    #time.sleep(5)
    

   # for index_counter in tweet.entities:
    #    print(tweet.entities.)
    
        
        
        
        
        
        #ment_dict[tweet.id]=


#key = "somekey"
#a.setdefault(key, [])
#a[key].append(1)
#a[key].append(2)

#petshop_dict = defaultdict(list)
#for key, value in petshop: 
#    petshop_dict[key].append(value)

   # squares = {1: 1, 2: 4, 3: 9}
#squares[4] = 16

#dict_keys(['hashtags', 'mentions', 'annotations'])
#dict_keys(['hashtags', 'mentions', 'annotations'])
#dict_keys(['hashtags', 'mentions', 'annotations'])
#dict_keys(['urls', 'mentions'])
#dict_keys(['urls', 'mentions'])
#dict_keys(['mentions', 'annotations'])
#dict_keys(['mentions', 'annotations'])
#dict_keys(['mentions', 'annotations'])
#dict_keys(['mentions', 'annotations'])
#dict_keys(['mentions'])
#dict_keys(['mentions'])
#dict_keys(['hashtags', 'mentions'])
#dict_keys(['hashtags', 'mentions'])
#dict_keys(['mentions'])
#dict_keys(['hashtags', 'mentions'])
#dict_keys(['hashtags', 'mentions'])
#dict_keys(['mentions'])



#s = [('rome', 1), ('paris', 2), ('newyork', 3), ('paris', 4), ('delhi', 1)]
#data_dict = {}
#for x in s:
#    data_dict.setdefault(x[0],[]).append(x[1])
#print(data_dict)
#Output:

#{'rome': [1], 'paris': [2, 4], 'newyork': [3], 'delhi': [1]}

#from collections import defaultdict
#i = 0
#mentions_dict = defaultdict(list)
#for tweet in response.data: 
#      print(tweet.entities.hashtags)
 # makieitastring(temp)
  #print(temp)
 # i = i + 1



  
    
    #tweet_id_container = tweet.id
    #for entities in tweet:
     #    print(entities)
        #mentions_dict[tweet_id_container].append(username("screen_name"))
#print(mentions_dict)
        #print(username)
        #for user_mentions in entities:
        #  print(user_mentions[0
       # mentions_dict[tweet_id_container].append(str(name))
      #if m != None:
         #mentions_dict[tweet_id_container].append(m['username'])
    #if 'mentions' in tweet.entities:
      #hashtag[text.id].append()
      #for usermentioned in tweet.entities['mentions']:
        #tweetid_str = str(tweet.id)
        #print(tweetid_str + ": " + usermentioned['username'])
#result = hydrate_search_recent_tweet_data(response)
#print(result)


# Defining the dict
#d = defaultdict(def_value)
#d["a"] = 1
#d["b"] = 2

#key = "somekey"
#a.setdefault(key, [])
#a[key].append(1)
#for n in n1:
#    if # condition #
#        if key not in dict:
#            dict[key] = []
#        dict[key].append(value)
#        print dict

#tweets = response

#print(tweets["Hashtags"])
#for s in range(len(tweets['Hashtags'])):
#      hasht=[]
#      for t in range(len(tweets.Hashtags[s])):
#         print(tweets['Hashtags'][s][t]['text'])
#         hasht.append(tweets['Hashtags'][s][t]['text'])
#         t=t+1
#      ht.append(hasht)
#      s=s+1
#tweets['HT']=zip(ht)
 




#for tweet in response:
#for tweets in response: # if "entities" in tweet and "hashtag" in tweet["entities"]:
 # for hashtag in tweets("entities")("hashtags"):
  #   print((hashtag["tag"]))
 #    time.sleep(10)


#userinfo = result
#for item in userinfo.items():
 #   print(item)
#f = open("userdict.txt", "w", encoding="utf-8")

#print(key,':',value) for key, value in result()
#f.write(makeitastring)
#f.close()
#for key, value in result.item():
#    f.write(response)
#f.close




#response = client.search_recent_tweets(query=query,
#                                       tweet_fields=['context_annotations','created_at','public_metrics'],
#                                       user_fields=['profile_image_url','description','location','public_metrics'], 
#                                       expansions='author_id',
#                                       max_results=10)



#def tweet_sentiment_hydrate(response):
   # analyzer = SentimentIntensityAnalyzer()
   # tweet_sentiment_array = []
   # avg_sentiment_array = []
   # for tweet in response.data:
        
    #    clean_tweet = p.clean(tweet.text)
    #result.append(p.clean(tweet_body))
        #tweet_sentiment_array.append(clean_tweet)
    
     #   vs = (analyzer.polarity_scores(clean_tweet))

        #tweet_sentiment_array.append(vs)
      #  avg_sentiment_array.append(vs)
       # print(clean_tweet)
    #print('vs')
    #print(clean_tweet)
    #print(vs)   
    #polarity_string = ''.join(map(str, vs))
    #arr = np.append([clean_tweet, vs])

    #a_2d_list.append([5, 6])
    #arr2 = np.append(vs)
    #tweetwithsentiment = clean_tweet+polarity_string   
    #fvader.write(tweetwithsentiment)
    #fvader.write(polarity_string)
    #print(len(arr))
    #hhh = analyzer.polarity_scores(avg_sentiment_array[20])
    
    #print(avgsentscores)
    #return (avgsentscores)


#tweet_sentiment_hydrate(response)
#print(h)







    
  
#fvader.close
#print('vs all up')
#print(len(arr))

#print(analyzer.polarity_scores(vs))         

# //todo #5 

#USER_ID = "potus"
#pers = "sales"
#message = result
#makeitastring = ''.join(map(str, message))



#f = open("humantic_tweets.txt", "w", encoding="utf-8")

#f.write(makeitastring)
#f.close()

#fvader.close()


#send_personality_traits(USER_ID, message)


#for x in range(1, 45):

   # time.sleep(1)

   # print('waiting...')



#retrieve_personality_traits(USER_ID, pers


   







