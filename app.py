import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
import requests

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/movie", methods=["POST"])
def bucket_post():
    # sample_receive = request.form['sample_give']
    bucket_receive = request.form['bucket_give']
    
    count = db.bucket.count_documents({})
    num = count + 1
    
    doc = {
        'num': num,
        'bucket': bucket_recieve,
        'done': 0,
    
    }

    db.bucket.insert_one(doc)
    return jsonify({'msg':'data saved!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movie_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)