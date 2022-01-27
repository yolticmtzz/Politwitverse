import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAANh02yZK%2Bg2Ga9OaIGmo%2FdcBKwI4%3DoBVTm4dbV9EsX06kTvtAz5XjSCK222TAxusnGUposUxAGoEFqg')

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGPIWwEAAAAAQ6Wu3fVaVsdg4PHyN7ktSku8u8g%3DMWmLEo5o3YPP0HsKRrX5S1UcKAnemvF2UVPG5Sp6S2qXRFNB9j')

query = "from:nickbschroer -is:retweet lang:en"

response = client.search_recent_tweets(query, end_time="2022-01-27T01:01:35+00:00", expansions=['author_id'], max_results=10)
metadata = response.meta
next_token = metadata.get('next_token')
metadata = response.meta
while next_token is not None:
    for tweet in response.data: 
        print(tweet.id)
        print(tweet.created_at)
        print(tweet.text)
    print("----------------------------------------------------------------")
    response = client.search_recent_tweets(query,end_time="2022-01-27T01:01:35+00:00", expansions=['author_id'], max_results=10, next_token=next_token)
    metadata = response.meta
    next_token = metadata.get('next_token')
