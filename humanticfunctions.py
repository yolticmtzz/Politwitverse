import http.client
import os
import json
import requests

def send_personality_traits(USER_ID, message):
      API_KEY = 'chrexec_fe80f6f524bce628b039e123e4eea9e1' 
      BASE_URL = "https://api.humantic.ai/v1/user-profile/create"  # Base URL for create endpoint

      headers = {
        'Content-Type': 'application/json'
      }

      # API Key: required; get the API key from the environment variable or substitute it directly

      # Analysis ID: required; User profile link from LinkedIn or, User Email ID
      # or, for document or text, use any unique identifier. We suggest using a value that helps you identify the analysis easily.
      #USER_ID = "https://twitter.com/" + USER_NAME  # or, any unique identifier

      url = f"{BASE_URL}?apikey={API_KEY}&userid={USER_ID}"

      # text: required for text based input
      # Minimum 300 words is expected to provide personality insights for acceptable confidence level.
      data = {
          "text": message
      }

      payload = json.dumps(data)

      print(url)
      print(payload)
      print(headers)

      #response = requests.request("POST", url, data=payload, headers=headers)

      

      #print(response.status_code, response.text)








  



def retrieve_personality_traits(USER_ID, PERSONA):
    API_KEY = 'chrexec_fe80f6f524bce628b039e123e4eea9e1' 
    
    BASE_URL = "https://api.humantic.ai/v1/user-profile"  # Base URL for the FETCH endpoint
    headers = {
    'Content-Type': 'application/json'
    }

    # API Key: required; get the API key from the environment variable or substitute it directly


    # Analysis ID: required; should be same as the id used to create the analysis
    #USER_ID = "https://www.linkedin.com/in/ramanaditya"  # or, any unique identifier

    # Persona: optional; possible values: "sales", "hiring"
    url = f"{BASE_URL}?apikey={API_KEY}&id={USER_ID}&persona={PERSONA}"

    response = requests.request("GET", url, headers=headers)
    print(response.status_code, response.text)

    file = open("humantic.txt", "w")
    file.write(response.text)
    file.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    