import os
import tweepy

consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# lamy = api.get_user("yukihanalamy")
# for friend in lamy.friends():
#     print(friend.screen_name)

# friends = tweepy.Cursor(api.friends)
# for friend in friends.items():
#     print(friend.name)

# recent_tweets = api.user_timeline()
# for tweet in recent_tweets:
#     print(tweet.text)

# rushia = api.get_user(id='uruharushia')
# tweets = api.user_timeline(screen_name='uruharushia',
#                            count = 20,
#                            include_rts = False,
#                            tweet_mode = 'extended',
#                            exclude_replies = True
#                            )
# for x in tweets[:5]:
#     print(x.full_text)
#     print()

# ### Like a tweet
# tweet_id = "1357253177700098048"
# api.create_favorite(tweet_id)

tweets = api.user_timeline(screen_name = 'suisei_hosimati',
                           exclude_replies = True,
                           count = 20,
                           include_rts = True,
                           tweet_mode = 'extended'
                           )
for tweet in tweets:
    attr = dir(tweet)
    tweet_id = tweet.id
    favorited = tweet.favorited
    rtd = tweet.retweeted
    if not rtd:
        api.retweet(tweet_id)
    if not favorited:
        api.create_favorite(tweet_id)
    print(tweet.full_text)

    print("-------------------------------")




