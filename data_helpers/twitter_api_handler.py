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
from os.path import exists

class TwitterApiHandler:
    tweepy_client: tweepy.Client

    def __init__(self):
        # load api login data from .env file
        path_to_env = "./twitter_api.env" # might need to be fixed later
        path_to_user_env = "./twitter_user_signin.env"

        api_conf = dotenv_values(dotenv_path=path_to_env)

        api_key = api_conf["api_key"] # euqal to consumer_key
        api_secret = api_conf["api_secret"]

        access_token = ""
        access_token_secret = ""

        # check if user is already signed in
        if (exists(path_to_user_env)):
            print("signing you in")
            client_conf = dotenv_values(dotenv_path=path_to_user_env)

            access_token = client_conf["access_token"]
            access_token_secret = client_conf["access_token_secret"]

        else:

            # if user is not signed in:
            print("not signed in yet, creating login link...")

            oauth1_user_handler = tweepy.OAuth1UserHandler(
                api_key, api_secret, callback="oob"
            )

            print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

            verifier = input("Input PIN: ")

            access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)

            print(access_token)
            print(access_token_secret)

            # write accesstokens to file for later access
            to_file_parse = f"access_token={access_token}\naccess_token_secret={access_token_secret}"
            
            env_file = open(path_to_user_env, "w")
            env_file.write(to_file_parse)
            env_file.close()

        # create client session
        print("authentificating against twitter and creating client session")

        self.tweepy_client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        pass

if __name__ == "__main__":
    handler = TwitterApiHandler()