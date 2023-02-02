import random

# list of pre-defined reply messages
REPLY_MESSAGES = [
    "TATA BYE BYE KHATAM"
]

# get a random reply message
def get_reply_message():
    return random.choice(REPLY_MESSAGES)
