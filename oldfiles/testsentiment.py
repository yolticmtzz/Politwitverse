
from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="en")

from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from pysentimiento.preprocessing import preprocess_tweet

query = "I REALLY don't want to write my review tonight. :("

vanalyzer = SentimentIntensityAnalyzer()

process_query = preprocess_tweet(query)
print(process_query)



print('bert')

print(analyzer.predict(process_query))


# returns AnalyzerOutput(output=POS, probas={POS: 0.998, NEG: 0.002, NEU: 0.000})
print('vader')
print(vanalyzer.polarity_scores(process_query))


