import os

# Twitter API credentials
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Keyword to search for in tweets
SEARCH_KEYWORD = "your_keyword"

# Log files
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
BOT_LOG_FILE = os.path.join(LOG_DIR, "bot.log")
ERROR_LOG_FILE = os.path.join(LOG_DIR, "errors.log")

# Data files
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
REPLIED_TO_FILE = os.path.join(DATA_DIR, "replied_to.txt")
STATE_FILE = os.path.join(DATA_DIR, "state.pickle")
