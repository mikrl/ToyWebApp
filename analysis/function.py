from pymongo import MongoClient

mongo = MongoClient("mongodb://172.17.0.2:27017").testdb


def readDB(idx):
    data = mongo.posts.find_one({'_id':idx})

    message, timestamp = data['message'], data['time']
    return (message, timestamp)

def getResponse(idx):
    message, timestamp = readDB(idx)
    return "You wrote: {0} on {1}".format(message, timestamp)
