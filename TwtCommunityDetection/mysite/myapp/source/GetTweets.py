import requests
import tweepy
import igraph
import networkx as nx
import json
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError, TwitterPager
import pandas as pd

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '994637543667851265-o2f0iiSrlbi2WZhT9ia5nQ8rQEFVJGf'
ACCESS_SECRET = 'GjDQZkRlZkhLqZANQiXt9sTILxAHoUdXvQIpl2aK1pVLu'
CONSUMER_KEY = 'NamqEpwbXC9zsTDQ4UlhTBCYZ'
CONSUMER_SECRET = 'HcMG8wpVIusTavefBhPYFQ5ZtveNzKDiJgC9cJ8HbGr5pR6IrQ'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAImLkAEAAAAApnd4R2sojla28VAGc4dBVbEtlT0%3D3oNrkzShnGapc5UId6jURBI29RXnM8PY7NMwjkoRs2ilfUOlbJ'

MAX_DEPTH = 5
json_data = []

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET)

user = client.get_user(username="SirCatDB")
def get_new_tweets(names):
    print("Retrieving tweets")
    corpus = []
    for name in names:
        followersResult = client.get_users_followers(id=user.data.id, max_results=100)
        print(followersResult)
        #time.sleep(4)
        corpus.extend(followersResult)
    data = [[tweet.id_str, tweet.user.screen_name, tweet.full_text, tweet.created_at] for tweet in corpus]
    tweets = pd.DataFrame(data, columns=['tweet_id', 'screen_name', 'text', 'timestamp'])
    print(tweets)

    return tweets

corpus = []
followersResult = client.get_users_followers(id=user.data.id, max_results = 100)
print(followersResult.data)

while('next_token' in followersResult.meta):
    followersResult = client.get_users_followers(id=user.data.id, max_results=1000, pagination_token=followersResult.meta['next_token'])
    print(followersResult.data)
    with open('../../../tweets.json', 'a+') as json_file:
        file_data = json.load(json_file)
        file_data[]
        json.dump(key['name'], json_file)



get_new_tweets(names)



""" Adds conversation_ids to the tweets retrieved from get_new_tweets
    Returns a data frame of the tweets with [id, screen_name, text, timestamp, conversation_id]
"""
def add_data(folowers):
    print("Retrieving additional data")
    ids = folowers.folower_id
    conv_ids = []
    for id in ids:

        TWEET_ID = id
        TWEET_FIELDS = 'conversation_id'

        try:
            r = twapi.request(f'tweets/:{TWEET_ID}', {'tweet.fields': TWEET_FIELDS})

            for item in r:
                conv_ids.append(item['conversation_id'])


        except TwitterRequestError as e:
            print(e.status_code)
            for msg in iter(e):
                print(msg)

        except TwitterConnectionError as e:
            print(e)

        except Exception as e:
            print(e)

    tweets['conversation_id'] = conv_ids
    return tweets