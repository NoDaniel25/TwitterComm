import pandas as pd
import csv
import time
import datetime

f = None
writer = None
dataset = None
filename = 'data.csv'
numberOfRows = 2
path = None


#Initialize Writer
def initializeWriter(filename, path):

    global f
    global writer
    f = open(path + filename + '.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(f)

def writeList(rowsToAdd):
    for key in rowsToAdd:
        writer.writerow(key)


def readDataset(filename):
    ds = pd.read_csv('../input/' + filename + ".csv", sep=',(?=\S)', engine='python')

    return ds

def delete_quotes(x):
    return x[1:-1]

def parseQuates(ds):
    # print(ds.head())

    for column in ["id", "screenName", "avatar", "lang", "tweetId"]:
        ds[column] = ds[column].apply(delete_quotes)

    return ds

def getRowsFromDataset(ds):
    ds = ds.drop(['tags', 'avatar', 'followersCount', 'friendsCount', 'lang', 'lastSeen', 'tweetId'], axis=1)
    rowsToAdd = []

    for index, row in ds.iterrows():
        print(index)
        lenghtOfFriendsList = len(row['friends'])
        friends = row['friends'][2:lenghtOfFriendsList - 2]
        friends = friends.replace('"', '')
        friends = friends.replace(' ', '')
        friendsListAsString = friends.split(',')
        if lenghtOfFriendsList > 2:
            friendsList = [eval(x) for x in friendsListAsString]

        for key in friendsList:
            rowsToAdd.append([eval(row['id']), key])

    return rowsToAdd

def getNamesPerId(ds):

    ds = ds.drop(['tags', 'avatar', 'followersCount', 'friendsCount', 'lang', 'lastSeen', 'tweetId', 'friends'], axis=1)
    return ds.values.tolist()

def replaceNamesInCsv(rowsToWrite, namesToReplace):
    hasOriginName = 0
    hasFriendName = 0
    namesDict = dict(namesToReplace)
    namesToWrite = []
    for key in rowsToWrite:
        if str(key[0]) in namesDict:
            hasOriginName = 1
        if str(key[1]) in namesDict:
            hasFriendName = 1
        if hasOriginName == 1 and hasFriendName == 1:
            namesToWrite.append([namesDict[str(key[0])], namesDict[str(key[1])]])
        hasOriginName = 0
        hasFriendName = 0

    return namesToWrite


def cutDataset(ds, numberOfRows):
    return ds.iloc[:numberOfRows]


def createSmallDatasets(times):
    for item in times:
        print("Starting dataset loading for " + str(item) + " rows...")

        start_time = time.time()

        initializeWriter(str(item) + 'Test', '../output/numbers/')
        df = readDataset('data')
        df = parseQuates(df)
        df = cutDataset(df, item)
        rowsToWrite = getRowsFromDataset(df)
        namesToReplace = getNamesPerId(df)
        newnames = replaceNamesInCsv(rowsToWrite, namesToReplace)
        writeList(newnames)

        print("Dataset loaded in %s" % (time.time() - start_time))

def createPartialDataset(size):
    times = []
    print("Starting dataset loading and parsing for ", size,  " rows...")

    initializeWriter(str(size) + 'Test', '../output/numbers/')
    df = readDataset('data')
    df = parseQuates(df)
    df = cutDataset(df, size)
    rowsToWrite = getRowsFromDataset(df)
    namesToReplace = getNamesPerId(df)
    newnames = replaceNamesInCsv(rowsToWrite, namesToReplace)
    writeList(newnames)





