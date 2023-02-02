import tweepy
from config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# create a tweepy API object
def get_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

# check if a tweet contains a keyword
def tweet_contains_keyword(tweet, keyword):
    return keyword.lower() in tweet.text.lower()

# reply to a tweet
def reply_to_tweet(api, tweet, message):
    status = "@{0} {1}".format(tweet.user.screen_name, message)
    api.update_status(status=status, in_reply_to_status_id=tweet.id)

# like a tweet
def like_tweet(api, tweet):
    api.create_favorite(tweet.id)

# retweet a tweet
def retweet_tweet(api, tweet):
    api.retweet(tweet.id)
