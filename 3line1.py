import tweepy
import time
import os
from os import environ
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

trigger=OrTrigger([
    CronTrigger(hour='6-23', minute='*')
])

def job():
    ckey=environ['ckey']
    csecret=environ['csecret']
    atoken=environ['atoken']
    asecret=environ['asecret']

    auth=tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    user=api.me()

    search='"Line 3" from:TTCnotices'
    nrTweets=1

    for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
        try:
            print('Alert RTd')
            print(tweet.text)
            tweet.retweet()
            time.sleep(1)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
sched=BackgroundScheduler()
sched.add_job(job, trigger)

sched.start()