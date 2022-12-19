from __main__ import app
import dbconn
from flask import Flask,render_template,request,jsonify,redirect,session
from flask import json

from flask_session import Session
# import createUser

# app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

@app.route('/manageGroup')
def ManageUser():

    print(session.get('userName'))
    return "Manage Group"
