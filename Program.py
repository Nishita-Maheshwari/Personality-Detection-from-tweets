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
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        earchTerm = input("Enter Keyword/Tag to search about: ")
        NoOfTerms = int(input("Enter how many tweets to search: "))

        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

        csvFile = open('result.csv', 'a')

        csvWriter = csv.writer(csvFile)

        polarity = 0
        neuroticsm = 0
        extraversion = 0
        openness = 0
        conscientiousness = 0
        agreeableness = 0
        sickiness = 0
        nervousness = 0

        for tweet in self.tweets:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity

            if (analysis.sentiment.polarity == 0):
                nervousness += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                extraversion += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                neuroticsm += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                openness += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                agreeableness += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                conscientiousness += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                sickiness += 1
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        neuroticsm = self.percentage(neuroticsm, NoOfTerms)
        extraversion = self.percentage(extraversion, NoOfTerms)
        openness = self.percentage(openness, NoOfTerms)
        conscientiousness = self.percentage(conscientiousness, NoOfTerms)
        agreeableness = self.percentage(agreeableness, NoOfTerms)
        sickiness = self.percentage(sickiness, NoOfTerms)
        nervousness = self.percentage(nervousness, NoOfTerms)

        polarity = polarity / NoOfTerms

        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")
        if (polarity == 0):
            print("nervousness")
        elif (polarity > 0 and polarity <= 0.3):
            print("extraversion")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("neuroticsm ")
        elif (polarity > 0.6 and polarity <= 1):
            print(" openness")
        elif (polarity > -0.3 and polarity <= 0):
            print("agreeableness")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("conscientiousness")
        elif (polarity > -1 and polarity <= -0.6):
            print("sickiness")

        print()
        print("Detailed Report: ")
        print(str(neuroticsm) + "% people thought it was neuroticsm ")
        print(str(extraversion) + "% people thought it was extraversion")
        print(str(openness) + "% people thought it was  openness")
        print(str(conscientiousness) + "% people thought it was conscientiousness")
        print(str(agreeableness) + "% people thought it was agreeableness")
        print(str(sickiness) + "% people thought it was sickiness")
        print(str(nervousness) + "% people thought it was nervousness")

        self.plotPieChart(neuroticsm, extraversion, openness, conscientiousness, agreeableness, sickiness, nervousness,
                          searchTerm, NoOfTerms)

    def cleanTweet(self, tweet):







