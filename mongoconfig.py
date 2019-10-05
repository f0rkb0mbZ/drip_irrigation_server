from pymongo import MongoClient, errors

def connect():
    try:
        client = MongoClient("Your MongoDB Connection URL here")
        db = client.test
        if db:
            print('Connection Successful!')
        return client
    except errors.ConnectionFailure as e:
        print('Connection failed!'+ e)
        