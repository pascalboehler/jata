#
# twitter_api_handler.py
# jata
#
# Created by Pascal Boehler on 10.10.2022
# Copyright © 2020 Pascal Boehler. All rights reserved.
#

from tweet.py import Tweet
from dotenv import load_dotenv
from dotenv import dotenv_values

class TwitterApiHandler:

    def __init__():
        # load api login data from .env file
        path_to_env = "./twitter_api.env" # might need to be fixed later

        api_conf = dotenv_values(dotenv_path=path_to_env)

        api_key = api_conf["api_key"]
        api_secret = api_conf["api_secret"]
        bearer_token=api_conf["bearer_token"]
        
         

        pass