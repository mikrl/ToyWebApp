import json
from flask_pymongo import PyMongo
from flask import Flask
from flask import request, render_template
from analysis.function import getResponse
from datetime import date

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.17.0.2:27017/testdb"
mongo=PyMongo(app)

@app.route('/', methods=['GET'])
def landing():
    return render_template('./landing.html')

@app.route('/', methods=['POST'])
def my_form_post():

    message, timestamp = request.form['msg'], date.today()
    post = {"message":message, "time":timestamp.__str__()}
    post_id = mongo.db.posts.insert_one(post).inserted_id

    response = getResponse(post_id)

    return response
    
    
    #processed_text = text.upper()
    #return processed_text
