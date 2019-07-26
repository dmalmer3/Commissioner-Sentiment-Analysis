# This program pulls the sentiment scores of each commissioner from the 
# dataframe and stores them in a list. It then counts how many occurrences
# of each score there for each commissioner and then scores these totals
# in a list and plots them on a stacked bar graph using pygal.

import pygal
from pygal.style import Style

from commissioner_tweets import goodell_tweets, silver_tweets, manfred_tweets

def pull_sentiment(dataframe):
	"""
	Pulls the sentiment column from each dataframe and puts it in a 
	list.
	"""
	sentiment_list = [sentiment for sentiment in dataframe['sentiment']]
	
	return sentiment_list


# Creates a list of the sentiment results from each commissioner's dataframe.
goodell_sentiment = pull_sentiment(goodell_tweets)
silver_sentiment = pull_sentiment(silver_tweets)
manfred_sentiment = pull_sentiment(manfred_tweets)

# Counts occurrences of positive sentiment scores for each commissioner.
goodell_pos = goodell_sentiment.count(1)
silver_pos = silver_sentiment.count(1)
manfred_pos = manfred_sentiment.count(1)

# Counts occurrences of neutral sentiment scores for each commissioner.
goodell_neutral = goodell_sentiment.count(0)
silver_neutral = silver_sentiment.count(0)
manfred_neutral = manfred_sentiment.count(0)

# Counts occurrences of negative sentiment scores for each commissioner.
goodell_neg = goodell_sentiment.count(-1)
silver_neg = silver_sentiment.count(-1)
manfred_neg = manfred_sentiment.count(-1)

# A list for each type of sentiment score.
pos_values = [goodell_pos, silver_pos, manfred_pos]
neutral_values = [goodell_neutral, silver_neutral, manfred_neutral]
neg_values = [goodell_neg, silver_neg, manfred_neg]

# Creates the graph of sentiment scores.
sentiment_plot = pygal.StackedBar()
sentiment_plot.title = 'Sentiment scores of 100 Tweets by league commissioners'
sentiment_plot.y_title = 'Frequency of score'
sentiment_plot.x_labels = 'Roger Goodell', 'Adam Silver', 'Rob Manfred'
sentiment_plot.add('Negative', neg_values)
sentiment_plot.add('Neutral', neutral_values)
sentiment_plot.add('Positive',  pos_values)

# Renders the plot to an svg file.
sentiment_plot.render_to_file('commissioner_sentiment.svg')
