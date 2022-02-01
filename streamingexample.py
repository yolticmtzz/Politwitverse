import tweepy
import os
import config


class tweetEntity:
    
    def __init__(self, entity):
        pass  
        
    def hydrate(tweet_entities):

          if 'mentions' in ent_dict:
                  t_mentions = ent_dict.get('mentions')
                  tweet_mentions = mention_hydrate(t_mentions) #
                  tweet_mentions = makeitastring(tweet_mentions)
                          
          else:
                  tweet_mentions = empty        
                      
          if 'hashtags' in ent_dict is not None: #is not None needed????
                  t_hashtags = ent_dict.get('hashtags')  
                  tweet_hashtags = hashtag_hydrate(t_hashtags) #
                  tweet_hashtags = makeitastring(tweet_hashtags)
                      
          else:
                  tweet_hashtags = empty

          if 'annotations' in ent_dict:
                  t_annotations = ent_dict.get('annotations')   
                  tweet_annotations = annotations_hydrate(t_annotations) #
                  tweet_annotations = makeitastring(tweet_annotations)

          else:
                  tweet_annotations = empty

          if 'urls' in ent_dict:
                  t_urls = ent_dict.get('urls')
                  tweet_urls = url_hydrate(t_urls) #
                  tweet_urls = makeitastring(tweet_urls)
          else:
                  tweet_urls = empty
                 
          return tweet_mentions, tweet_hashtags, tweet_annotations, tweet_urls  

   
# Driver Code
streamdata = Hydrator("12345)")
streamdata.clean_tweets("I dont know #how to do this")
print(streamdata.getCleanTweet())

# class Dog:
       
#     # Class Variable
#     animal = 'dog'     
       
#     # The init method or constructor
#     def __init__(self, breed):
           
#         # Instance Variable
#         self.breed = breed            
   
#     # Adds an instance variable 
#     def setColor(self, color):
#         self.color = color
       
#     # Retrieves instance variable    
#     def getColor(self):    
#         return self.color   
   
# # Driver Code
# Rodger = Dog("pug")
# Rodger.setColor("brown")
# print(Rodger.getColor()) 



# # # Subclass Stream to print IDs of Tweets received
# # class IDPrinter(tweepy.Stream):

# #     def on_status(self, status):
# #         print(status.id)



# # # Initialize instance of the subclass
# # printer = IDPrinter(
# #   config.consumer_key, config.consumer_secret,
# #   config.access_token, config.access_token_secret
# # )

# # # Filter realtime Tweets by keyword
# # printer.filter(track=["Twitter"])