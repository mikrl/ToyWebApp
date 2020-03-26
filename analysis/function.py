from pymongo import MongoClient

mongo = MongoClient("mongodb://mongo_database/user_database")


def readDB(idx):
    data = mongo.user_database.posts.find_one({'_id':idx})

    message, timestamp = data["message"], data["time"]
    return (message, timestamp)

def getResponse(idx):
    message, timestamp = readDB(idx)
    return "You wrote: {0} on {1}".format(message, timestamp)
