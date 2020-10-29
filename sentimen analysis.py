import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_csv('merged_file.csv')
analyser = SentimentIntensityAnalyzer()


def sentiment_analysis(text):
    return analyser.polarity_scores(text)


sentiment = [None] * len(data['Purpose'])
for i in range(len(data['Purpose'])):
    sentiment[i] = sentiment_analysis(data['Purpose'][i])['compound']

best_idea = sentiment.index(max(sentiment))
worst_idea = sentiment.index(min(sentiment))
best_idea = data['Purpose'][best_idea]
worst_idea = data['Purpose'][worst_idea]

print('The best idea is "%s".' % best_idea)
print('The worst idea is "%s".' % worst_idea)
