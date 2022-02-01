import tweepy
import os
import config
from twitclass import Hydrator



   
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