#
# twitter_api_handler.py
# jata
#
# Created by Pascal Boehler on 10.10.2022
# Copyright © 2020 Pascal Boehler. All rights reserved.
#

from tweet import Tweet
from dotenv import load_dotenv
from dotenv import dotenv_values
import tweepy

class TwitterApiHandler:

    def __init__(self):
        # load api login data from .env file
        path_to_env = "./twitter_api.env" # might need to be fixed later

        api_conf = dotenv_values(dotenv_path=path_to_env)

        api_key = api_conf["api_key"] # euqal to consumer_key
        api_secret = api_conf["api_secret"]

        oauth1_user_handler = tweepy.OAuth1UserHandler(
            api_key, api_secret, callback="oob"
        )

        print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

        verifier = input("Input PIN: ")

        access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)

        print(access_token)
        print(access_token_secret)

        pass

if __name__ == "__main__":
    handler = TwitterApiHandler()