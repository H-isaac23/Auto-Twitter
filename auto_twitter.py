import os
import tweepy


def favorite_tweet(t_id, ftd):
    if not ftd:
        api.create_favorite(t_id)


def retweet(t_id, rtd):
    if not rtd:
        api.retweet(t_id)


consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

screen_name = 'minatoaqua'

tweets = api.user_timeline(screen_name=screen_name,
                           exclude_replies=True,
                           count=20,
                           include_rts=True,
                           tweet_mode='extended'
                           )

for tweet in tweets:
    favorited = tweet.favorited
    retweeted = tweet.retweeted
    tweet_id = tweet.id

    favorite_tweet(tweet_id, favorited)
    retweet(tweet_id, retweeted)
