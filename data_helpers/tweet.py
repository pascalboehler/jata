#
# tweet.py
# jata
#
# Created by Pascal Boehler on 10.10.2022
# Copyright © 2020 Pascal Boehler. All rights reserved.
#


class Tweet:

    tweeter: str = ""
    tweet_id: int = 120
    tweet_content: str = "This is a tweet"
    like_count = 12
    retweet_count = 12
    comment_count = 12


    def __init__():
        print("Hi")

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