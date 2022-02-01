import requests
import os
import json
import requests
import time
import os
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
bearer_token = config.bearer_token

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = bearer_token
print(bearer_token)


search_url = "https://api.twitter.com/2/tweets/search/recent"
clist = []

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
params = {
    "query": "conversation_id:1487526628674748420",
    "tweet.fields": "author_id,context_annotations",
    "user.fields": "name,location,description,created_at",
    "expansions": "author_id",
}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
print(response.status_code)
