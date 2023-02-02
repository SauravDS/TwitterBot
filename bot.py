import tweepy
import helpers
import reply_message
from config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# set the keyword to search for in tweets
KEYWORD = "Aadani Eterprise"

# authenticate to the Twitter API using tweepy
def authenticate():
    api = helpers.get_api()
    return api

# search for tweets containing the keyword
def search_tweets(api, keyword):
    return tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items(10)

# main function
def main():
    api = authenticate()
    tweets = search_tweets(api, KEYWORD)

    for tweet in tweets:
        if not tweet.retweeted and not tweet.in_reply_to_status_id:
            if helpers.tweet_contains_keyword(tweet, KEYWORD):
                message = reply_message.get_reply_message()
                helpers.reply_to_tweet(api, tweet, message)

if __name__ == '__main__':
    main()
