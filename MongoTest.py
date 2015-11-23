import pymongo

from pymongo import MongoClient

connection=MongoClient('localhost',27017)

db=connection.mongtest

names=db.things

item=names.find_one()

print item['b']
