from pymongo import MongoClient
uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)
db = client.training
collection = db.mongodb_glossary
documents_to_insert = [
{"database": "a database contains collections"},
{"collection": "a collection stores the documents"},
{"document": "a document contains the data in the form of key-value pairs."},
]
collection.insert_many(documents_to_insert) 
documents_all = collection.find()
for document in documents_all:
 print(document)
client.close()