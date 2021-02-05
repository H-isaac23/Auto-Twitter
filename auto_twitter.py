import os
import tweepy

consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

with open("screen names.txt", 'r') as f:

    for name in f.readlines():
        screen_name = None
        if name[-1] == "\n":
            screen_name = name[:-1]
        else:
            screen_name = name

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
                api.retweet(tweet_id)
            if not favorited:
                api.create_favorite(tweet_id)
                print(tweet.full_text)
                print('-----------------------------------------------------')
