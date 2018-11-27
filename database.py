import pymongo


# inheriting from object

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # if you are not using self, then mention as static method
    # not gonna use self bcoz this method only belongs to Database class and never to its instance
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['new_db']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
