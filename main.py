import tweepy

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

pubic_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)
