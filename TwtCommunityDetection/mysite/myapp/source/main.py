import csv

import requests
import tweepy
import igraph
import networkx as nx
import json
import pandas as pd
#import iGraph
import FollowersActions as fls
import graphUtils as gutils


username = "RaduNamPleaca"
level = 3



#fls.createCsvFile(username + "_" + str(level))
#listOfRows = fls.getFollowers(username, level)
#fls.writeFollowersToCsv(listOfRows)

#currentLevelFollowersToRetrieve = []
#fls.getLimit()

gutils.plotGraphGN("../output/numbers/2000Test.csv")


#fls.testFollow()

#print(currentLevelFollowersToRetrieve)

#print(listOfRows[0][0])


#ds = pd.read_csv('data.csv', sep=',(?=\S)', engine='python')
#print(ds.head())

#def delete_quotes(x):
#    return x[1:-1]

#for column in ["id", "screenName", "avatar", "lang", "tweetId"]:
#    ds[column] = ds[column].apply(delete_quotes)

#ds = ds.iloc[:2]
#ds = ds.drop(['tags', 'avatar', 'followersCount', 'friendsCount', 'lang', 'lastSeen', 'tweetId'], axis = 1)
#print(twiter_data["friends"])

#print(ds)



'''
for index, row in ds.iterrows():
    print(index)
    lenghtOfFriendsList = len(row['friends'])
    friends = row['friends'][2:lenghtOfFriendsList-2]
    friends = friends.replace('"', '')
    friends = friends.replace(' ', '')
    friendsListAsString = friends.split(',')
    if lenghtOfFriendsList > 2:
        friendsList = [eval(x) for x in friendsListAsString]

    for key in friendsList:
        rowsToAdd.append([eval(row['id']), key])

global f
global writer
f = open("test" + '.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(f)

for key in rowsToAdd:
    writer.writerow(key)

#print(rowsToAdd)

'''



'''
followersResult = client.get_users_followers(id=user.data.id, max_results = 100)
#print(followersResult)
for key in followersResult.data:
    #print(key)
    node1 = TreeNode(key)
    node.add_child(node1)

node.traverse(0)
'''
"""
while('next_token' in followersResult.meta):
    followersResult = client.get_users_followers(id=user.data.id, max_results=1000, pagination_token=followersResult.meta['next_token'])
    print(followersResult.data)
    with open('tweets.json', 'a+') as json_file:
        file_data = json.load(json_file)
        file_data[]
        json.dump(key['name'], json_file)
"""

#asd3 = client.get_users_followers(id=asd.data.id, max_results = 1000, pagination_token=asd2.meta['next_token'])

#print(asd3)



#for key in asd2.data:
#    print(key)




