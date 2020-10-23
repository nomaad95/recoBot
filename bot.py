import shutil
import requests
import tweepy
import sys
import os
from classification import *
from apikey import key
from signature import *

recobot()


keys = key() # No offense but I am not confortable with sharing my API keys on github...
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tweepy.API(auth, wait_on_rate_limit=True)
public_tweets = api.home_timeline()
print("auth ok")

timeline = api.home_timeline()

user = api.get_user("archillect")
print(user.name)


last_tweet = ""
while(True):
    status = api.user_timeline("archillect", count=1)[0]
    for media in status.entities.get("media",[{}]):
        if media.get("type",None) == "photo" and status.id != last_tweet:
            last_tweet = status.id
            tweet_id = status.id
            print(tweet_id)
            print(media["media_url"])
            image = requests.get(media["media_url"])
            if image.status_code==200:
                image.raw.decode_content=True
                with open("arch.jpg",'wb') as f:
                    f.write(image.content)
                    reply = tweet('arch.jpg')
                    api.update_status(reply, tweet_id)
                    print(reply)
                    print("waiting...")

            else:
                print("coudn't download")
