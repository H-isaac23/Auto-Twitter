from threading import Thread
import os
import tweepy
import time

consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def auto(screen_name):
    tweets = api.user_timeline(screen_name=screen_name,
                               exclude_replies=True,
                               count=7,
                               include_rts=True,
                               tweet_mode='extended'
                               )

    for tweet in tweets:
        favorited = tweet.favorited
        retweeted = tweet.retweeted
        tweet_id = tweet.id

        if not retweeted:
            try:
                api.retweet(tweet_id)
            except tweepy.error.TweepError:
                print("Tweet already retweeted.")

        if not favorited:
            try:
                api.create_favorite(tweet_id)
            except tweepy.error.TweepError:
                print("Tweet already favorited")
        print(tweet.full_text)
        print('-----------------------------------------------------')

with open("screen names.txt", 'r') as f:

    threads = []
    screen_names = f.readlines()

    for screen_name in screen_names:
        if screen_name[-1] == "\n":
            screen_name = screen_name[:-1]
        threads.append(Thread(target=auto, args=(screen_name,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
