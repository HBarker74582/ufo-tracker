from flask import Flask, render_template, redirect, jsonify, request
import os
import requests
import json

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
import pandas as pd


# Create an instance of our Flask app.
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/UFO"
mongo = PyMongo(app)

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable


# render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html")

    # Redirect back to home page
    return redirect("/")

# @app.route("/mongo_data")
# def import_csvfile():
#     ufo_data = mongo.db.ufo1

@app.route("/alien_data")
def data():
    alien_collection = mongo.db.alien_data.find({})
    alien_data_json = []
    for json in alien_collection:
        alien_data_dict = {}
        alien_data_dict.update({
            "state_long": json["state_long"],
            "state_short": json["state_short"],
            "city_state": json["city_state"],
            "mj_legal": json["mj_legal"],
            "lat": json["lat"],
            "long" : json["long"],
            "sighting_date" : json["sighting_date"]

        })
        alien_data_json.append(alien_data_dict)

    return jsonify(alien_data_json)

@app.route("/military")
def military():
    military_basescollection = mongo.db.military_bases.find({})
    military_bases_json = []
    for json in military_basescollection:
        military_bases_dict = {}
        military_bases_dict.update({
            "state_long": json["state_long"],
            "state_short": json["state_short"],
            "mil_base_name" : json["mil_base_name" ],
            "component" : json["component"],
            "lat": json["lat"],
            "long" : json["long"],
            "country": json["country"]
        })
        military_bases_json.append(military_bases_dict)
    return jsonify(military_bases_json)

@app.route("/sightings")
def sightings():
    sightings_collection = mongo.db.sightings_count.find({})
    sightings_json = []
    for json in sightings_collection:
        sightings_dict = {}
        sightings_dict.update({
            "state_long": json["state_long"],
            "state_short": json["state_short"],
            "sightings_total" : json["sightings_total"],
            "Jan" : json["Jan"],
            "Feb" : json["Feb"],
            "Mar" : json["Mar"],
            "Apr" : json["Apr"],
            "May" : json["May"],
            "Jun" : json["Jun"],
            "Jul" : json["Jul"],
            "Aug" : json["Aug"],
            "Sep" : json["Sep"],
            "Oct" : json["Oct"],
            "Nov" : json["Nov"],
            "Dec" : json["Dec"],
        })
        sightings_json.append(sightings_dict)
    return jsonify(sightings_json)

@app.route("/word_cloud")
def word_cloud():
    word_cloud_collection = mongo.db.word_cloud_usatotals.find({})
   # print([json for json in word_cloud_collection])
    word_cloud_json = []
    for json in word_cloud_collection:
        word_cloud_dict = {}
        word_cloud_dict["word"] =  json["word"]
        word_cloud_dict.update({
            "word": json["word"],
            "count": json["count"]
    })
        word_cloud_json.append(word_cloud_dict)

    return jsonify(word_cloud_json)

if __name__ == "__main__":
    app.run(debug=True)

