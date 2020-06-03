import tweepy
import time
import os
from os import environ

ckey=environ['ckey']
csecret=environ['csecret']
atoken=environ['atoken']
asecret=environ['asecret']

auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()

search='"Line 3" from:TTCnotices'
nrTweets=5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Alert RTd')
        print(tweet.text)
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
