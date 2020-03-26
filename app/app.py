import json
from flask import Flask
from flask import request, render_template
from flask_pymongo import PyMongo
from analysis.function import getResponse
from datetime import date

app = Flask(__name__)

#app.config['MONGO_HOST'] = 'mongo_database'
#app.config['MONGO_PORT'] = '27017'
#app.config['MONGO_DBNAME'] = 'user_database'
#app.config['MONGO_USERNAME'] = 'application'
#app.config['MONGO_PASSWORD'] = 'apppassword'
#app.config['MONGO_AUTH_SOURCE'] = 'admin'
#app.config["MONGO_URI"] = 'mongodb://mongo_database'
app.config["MONGO_URI"] = 'mongodb://mongo_database/user_database'
#app.config["MONGO_URI"] = 'mongodb://root:password@mongo_database:27017/user_database?authSource=admin'
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
