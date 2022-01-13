
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')
from nltk.corpus import twitter_samples
analyzer = SentimentIntensityAnalyzer()




def get_avg_sentiment(preprocessed_tweets):
    arr10 = []
    arr10 = [preprocessed_tweets]

    mystr = analyzer.polarity_scores(arr10)

    return mystr




#The output is 70.7% neutral ad 29.3% negative. The compound score is -0.6597


#{'neg': 0.293, 'neu': 0.707, 'pos': 0.0, 'compound': -0.6597}