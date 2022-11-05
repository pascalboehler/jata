#
# main.py
# jata
#
# Created by Pascal Boehler on 10.10.2022
# Copyright © 2020 Pascal Boehler. All rights reserved.
#

from data_helpers.twitter_api_handler import TwitterApiHandler

if __name__ == '__main__':
    ApiHandler = TwitterApiHandler()

    ApiHandler.getUserTimeline()
