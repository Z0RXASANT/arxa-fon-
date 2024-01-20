from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://KhanSafarov:SwCSJXhtb9B6nAv6@kitabifydb.okhfdb5.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URL)

for db_name in client.list_database_names():
    print(db_name);