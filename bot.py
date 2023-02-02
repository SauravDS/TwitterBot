import tweepy

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize tweepy API
api = tweepy.API(auth)

# Search for tweets containing the keyword
tweets = api.search(q="keyword", tweet_mode="extended")

# Reply to each tweet containing the keyword
for tweet in tweets:
    username = tweet.user.screen_name
    status_id = tweet.id

    # Compose the reply
    reply = "@" + username + " thank you for mentioning the keyword!"

    # Post the reply
    api.update_status(status=reply, in_reply_to_status_id=status_id)
