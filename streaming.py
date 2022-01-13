import tweepy

API_KEY = "anvCaAUUuYqG3xLR7dNAzR0dr"
API_SECRET_KEY = "ULtEkEdycJzC08cyebSg1ExdOVgCg5pUG0qtLPnLta24ClNDqr"
ACCESS_TOKEN = "1469761271709028359-FrJt9sku3toFacDx1tdvmSPc273pKf"
ACCESS_TOKEN_SECRET = "mlblwNEQ21A6IrmC4boX42Rctpq0WLNMfTsoOSmOwPrAa"

stream = tweepy.Stream(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)



class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)
        print(status.text)
        print(status.entities)
        print(status.user.screen_name)



printer = IDPrinter(
  API_KEY, API_SECRET_KEY,
  ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
printer.filter(track=['missouri teachers'],languages = ["en"])


