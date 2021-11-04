""" Collect the tweets from a certain hashtag """
import csv
import os

import tweepy

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_SECRET")

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(AUTH, wait_on_rate_limit=True)

with csv.writer(open("../data/tweets.csv", "w")) as writer:

    tweets = tweepy.Cursor(
        API.search, q="#EURO2021", lang="en", since="2017-04-03"
    ).items(500)

    for tweet in tweets:
        writer.writerow([tweet.user.screen_name, tweet.text, tweet.user.location])
