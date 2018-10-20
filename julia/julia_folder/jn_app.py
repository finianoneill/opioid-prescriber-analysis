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
conn = 'mongodb://localhost:27017'
#conn = 'mongodb+srv://fin_database:findbpass@cluster0-kyr7n.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(conn)

# Define mongo database and collection
#mongo_db = client.opiod_physician_db
#collection = mongo_db.items
db = client.overdose_db
collection = db.state_overdoses

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
        f"/api/v1.0/overdose<br/>"
    )


@app.route("/api/v1.0/overdose")
def overdose():
	"""Expose the results of the mongo DB as a giant JSON for the user to pull from."""
	# extract the latitude and longitude coordinates for each physician into a final data frame
	# the previous loops do not need to be executed if latitude and longitude coordinates
	# are already stored in the mongo db
	df_columns = ['State', 'Total Number of Deaths', 'Number of Drug Overdose Deaths', '% of Drug Overdose Deaths', 'Opioid Overdose Deaths', 'Heroin Overdose Deaths', 'Natural & Semi-synthetic Opioid Overdose Deaths', 'Synthetic Opioid Deaths (excl. methadone)', 'Methadone Overdose Deaths']
	overdose_df = pd.DataFrame(columns=df_columns)

	return jsonify(overdose_df.to_dict('dict'))


if __name__ == '__main__':
    app.run(debug=True)
