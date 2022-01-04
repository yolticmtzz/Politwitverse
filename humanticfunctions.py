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

      response = requests.request("POST", url, data=payload, headers=headers)

      print(response.status_code, response.text)






  



def retrieve_personality_traits(SOCIAL_USER_NAME, SOCIAL_PROFILES, HUMANTIC_ID, message, PERSONA):
    API_KEY = 'chrexec_fe80f6f524bce628b039e123e4eea9e1' 
    conn = http.client.HTTPSConnection("api.humantic.ai")

    FETCH_ENDPOINT = "/v1/user-profile"  # FETCH endpoint
    headers = {
    'Content-Type': 'application/json'
    }

    url = f"{FETCH_ENDPOINT}?apikey={HUMANTIC_API_KEY}&id={HUMANTIC_ID}&persona={PERSONA}&username={SOCIAL_USER_NAME}&social_profiles{SOCIAL_PROFILES}"
    payload = {}
    print(url)

    conn.request("GET", url, payload, headers)
    response = conn.getresponse()
    #status_code = response.status
    data = response.read()
    #print(status_code, data.decode("utf-8"))
    #print(data.decode("utf-8"))

    f = open("humantic" + HUMANTIC_ID + ".txt", "w")
    f.write(data.decode("utf-8"))
    f.close()


