import tweepy

# Replace these with your own X API credentials
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
ACCESS_TOKEN = "your_access_token_here"
ACCESS_TOKEN_SECRET = "your_access_token_secret_here"

# Authenticate with X API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Post a status update
try:
    api.update_status("Hello, world! Posted by my bot.")
    print("Status posted successfully!")
except tweepy.TweepyException as e:
    print(f"Error posting status: {e}")