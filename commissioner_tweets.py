# This program searches Twitter for Tweets containing each commissioner's 
# name and uses sentiment analysis to return a value of 1, 0, or -1 to 
# classify the Tweet as positive, neutral, or negative and stores the 
# Tweet and sentiment score in a dataframe.

from tweepy import OAuthHandler
from tweepy import API

from textblob import TextBlob

import twitter_credentials
import pandas as pd
import numpy as np
import re

# Authorizes use of Twitter API
auth = OAuthHandler(twitter_credentials.consumer_key, 
			twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, 
	twitter_credentials.access_token_secret)
api = API(auth)

class TweetAnalyzer():
	"""Finds tweets and analyzes their sentiment."""
	
	def clean_tweet(self, tweet):
		"""Removes all special characters from a tweet."""
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
	
	def analyze_sentiment(self, tweet):
		"""Analyzes the sentiment of a tweet."""
		analysis = TextBlob(self.clean_tweet(tweet))
		
		if analysis.sentiment.polarity > 0:
			return 1
		elif analysis.sentiment.polarity == 0:
			return 0
		else:
			return -1
	
	def get_tweets(self, name):
		"""
		Finds tweets containing the name and store them in a dataframe.
		"""
		tweets = api.search(name + '-filter:retweets', count=100)
		
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])
		df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
		
		return df

# Creates TweetAnalyzer instance and creates data frames for commissioners.
tweet_analyzer = TweetAnalyzer()
goodell_tweets = tweet_analyzer.get_tweets('roger goodell')
silver_tweets = tweet_analyzer.get_tweets('adam silver')
manfred_tweets = tweet_analyzer.get_tweets('rob manfred')


	
	






