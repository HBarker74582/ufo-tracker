from flask import Flask, render_template, redirect
from pymongo import MongoClient
import csv
import pandas as pd
import json
import os

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import pymongo

def import_csvfile(filepath):
    mongo_client = pymongo.MongoClient('localhost', 27017)
    mongo_db = mongo_client['UFO1']
    db_collection = mongo_db[sightings_count]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res)
    data_json = json.load(data.to_json(orient='records'))
    db_collection.insert(data_json)


    filepath = "data/sightings_count.csv"
    import_csvfile(filepath)
    print(filepath)

# connection = MongoClient()
# db = connection.UFO1

# sightings_count = db.sightings_count
# df = pd.read_csv("data/sightings_count.csv")
# records = df.to_dict(orient = 'state_long' )
# result = db.sightings_count.insert_many(records)
