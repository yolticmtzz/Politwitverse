import twint

import nest_asyncio
nest_asyncio.apply()
c = twint.Config()
c.Search = "missouri education -is:retweet"
# Custom output format

c.Username = "dingersandks"

twint.run.Followers(c)
