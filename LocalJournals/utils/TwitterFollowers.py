#! /usr/bin/env python

import oauth2 as oauth
import json
import pandas as pd



CONSUMER_KEY = 'Consumer Key Goes Here'
CONSUMER_SECRET = 'Consumer Secret Goes Here'
ACCESS_KEY = 'Access Key Goes Here'
ACCESS_SECRET = 'Access Secret Goes Here'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)


def twitter_get_info(user):

    followers = None
    suspended = None

    user_endpoint = 'https://api.twitter.com/1.1/users/lookup.json?screen_name=' + user
    response, data = client.request(user_endpoint)

    user_data = json.loads(data)

    if isinstance(user_data, dict) == True:
        if user_data['errors'][0]['code'] == 17 or user_data['errors'][0]['code'] == 63:
            suspended ='Y'
            followers = None
            following = None
            statuses = None

        else:
            print("pass-errors but not suspended")
            pass

    elif isinstance(user_data, list) == True:
        followers = user_data[0]['followers_count']
        following = user_data[0]['friends_count']
        statuses = user_data[0]['statuses_count']

        suspended = None
    else:
        print("Other result--Review file")
        pass


    return followers, suspended, following, statuses


df = pd.read_csv('sites.csv', delimiter=",")
df['Twittersuspended?'] = ''

for index, row in df.iterrows():
    if isinstance(row['twitterUsername'], str) == True:
        foll, suspend, friends, tweets = twitter_get_info(row['twitterUsername'])
        df.at[index,'twitterFollowers'] = foll
        df.at[index, 'twitterFollowing'] = friends
        df.at[index, 'Twittersuspended?'] = suspend
        df.at[index, 'twitterTweets'] = tweets
    else:
        pass


df.to_csv('site2.csv')




