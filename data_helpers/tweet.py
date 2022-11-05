#
# tweet.py
# jata
#
# Created by Pascal Boehler on 10.10.2022
# Copyright © 2020 Pascal Boehler. All rights reserved.
#


class Tweet:

    tweet_id: int
    tweet_content: str
    tweeter: str = ""
    like_count = 12
    retweet_count = 12
    comment_count = 12


    def __init__(self, tweet_id: int, tweet_content: str = "Blablabla", tweeter: str = "placeholder", like_count: int=12, retweet_count: int = 12, comment_count: int = 23):
        self.tweet_id = tweet_id
        self.tweet_content = tweet_content
        self.tweeter = tweeter
        self.like_count = like_count
        self.retweet_count = retweet_count
        self.comment_count = comment_count

    ###########
    # getters #
    ###########

    def get_tweeter(self) -> str:
        return self.tweeter

    def get_tweet_id(self) -> int:
        return self.tweet_id

    def get_like_count(self) -> int:
        return self.like_count

    def get_retweet_count(self) -> int:
        return self.retweet_count

    def get_tweet_content(self) -> str:
        return self.tweet_content

    #################
    # tweet actions #
    #################

    def like_tweet(self):
        self.like_count += 1

    def retweet(self):
        self.retweet_count += 1

    def comment(self):
        self.comment_count += 1
        print("I comment something stupid")