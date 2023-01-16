import tweepy
import csv

ACCESS_TOKEN = '994637543667851265-o2f0iiSrlbi2WZhT9ia5nQ8rQEFVJGf'
ACCESS_SECRET = 'GjDQZkRlZkhLqZANQiXt9sTILxAHoUdXvQIpl2aK1pVLu'
CONSUMER_KEY = 'NamqEpwbXC9zsTDQ4UlhTBCYZ'
CONSUMER_SECRET = 'HcMG8wpVIusTavefBhPYFQ5ZtveNzKDiJgC9cJ8HbGr5pR6IrQ'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAImLkAEAAAAApnd4R2sojla28VAGc4dBVbEtlT0%3D3oNrkzShnGapc5UId6jURBI29RXnM8PY7NMwjkoRs2ilfUOlbJ'


client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit = 1)
f = None
writer = None

import requests


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    return r


def getLimit():
    bearer = "your bearer token"

    params = {"query": "your search"}

    response = requests.get("https://api.twitter.com/2/users/:id/followers", params=params, auth=bearer_oauth)

    print(response.headers)


def createCsvFile(fileName):
    global f
    global writer
    f = open(fileName + '.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(f)

def testFollow():

    auth = tweepy.OAuth1UserHandler(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )

    api = tweepy.API(auth)

    # Follow every follower of the authenticated user
    for follower in tweepy.Cursor(api.get_followers).items():
        follower.follow()

    for user in tweepy.Cursor(api.followers, screen_name="SirCatDB").items():
        print
        user.screen_name

def getFollowers(username, level):
    user = client.get_user(username=username)
    listOfRows = []



    followersResult = client.get_users_followers(id=user.data.id, max_results=1000)
    #print(followersResult)

    running = 1
    #while running:
    if followersResult.data is not None and level > 1:
        for key in followersResult.data:
            print(str(level) + " " + str(username) + " " + str(key))
            listOfRows.append([username, key])
            listOfRows.append(getFollowers(key, level - 1))
            #    listOfRows.append([username, key])
            #else:
            #    listOfRows.append(getFollowers(key, level - 1))
            #if 'next_token' in followersResult.meta :
            #    followersResult = client.get_users_followers(id=user.data.id, max_results=1000,
            #                                                 pagination_token=followersResult.meta['next_token'])
            #else:
            #    running = 0
        #else:
            #running = 1


    return listOfRows

def writeFollowersToCsv(followerList):
    for key in followerList:
        writer.writerow(key)




