import sys

import tweepy
import csv
import re
from textblob import TextBlob
import matplotlib.pyplot as plt


class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        # authenticating
        consumerKey = '8XjsAxfTrb5pYN3CQYjZaeHKo'
        consumerSecret = 'tZBko2hoVZ4RBVOrvUDqQBUlGAEgsnQDJ9reeapddedxhPvtjy'
        accessToken = '977420215700074496-EWusxwITCswztoob0qCDa6ZN7ffHHrQ'
        accessTokenSecret = 'cM0vmj0Xv2ScLJdDoxAjHSObwToWZBbSgzw9gGWPIf4wb'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)