import numpy as np
import datetime as dt

# import dependencies
import pandas as pd
import os
import requests
from datetime import datetime
import pymongo

from flask import Flask, jsonify
from flask import request


#################################################
# Database Setup
#################################################

# store each provider as an input in the mongo db
# Initialize PyMongo to work with MongoDBs
#conn = 'mongodb://localhost:27017'
conn = 'mongodb+srv://fin_database:findbpass@cluster0-kyr7n.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(conn)

# Define mongo database and collection
#mongo_db = client.opiod_physician_db
#collection = mongo_db.items
mongo_db = client.opioid_physician_db
collection = mongo_db.physicians

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/mongodbopioid<br/>"
    )


@app.route("/api/v1.0/mongodbopioid")
def mongodbopioid():
	"""Expose the results of the mongo DB as a giant JSON for the user to pull from."""
	# extract the latitude and longitude coordinates for each physician into a final data frame
	# the previous loops do not need to be executed if latitude and longitude coordinates
	# are already stored in the mongo db
	df_columns = ["npi", "physician_first_name", "physician_last_name",
	             "zip_code", "opioid_claim_count", "total_claim_count",
	             "specialty_description", "lat", "lng"]
	physician_coordinate_df = pd.DataFrame(columns=df_columns)

	row_counter = 0
	for document in collection.find():
	    if document["lng"] != "":
	        current_row_list = [document["npi"], document["physician_first_name"],
	                           document["physician_last_name"], document["zip_code"],
	                           document["opioid_claim_count"], document["total_claim_count"],
	                           document["specialty_description"], document["lat"],
	                           document["lng"]]
	        physician_coordinate_df.loc[row_counter] = current_row_list
	        row_counter += 1

	# create dictionary from the dataframe to serve up as JSON

	return jsonify(physician_coordinate_df.to_dict('dict'))


if __name__ == '__main__':
    app.run(debug=True)
