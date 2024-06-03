# Day 85 - Sessions

# from flask import Flask, request, redirect, session
# import os

# app = Flask(__name__)
# app.secret_key = os.environ['sessionKey']

# @app.route('/')
# def index():
#   page = ""
#   myName = ""
#   if session.get("myName"):
#     myName = session["myName"]
#   page += f"<h1>{myName}</h1>"
#   f = open("form.html", "r")
#   page += f.read()
#   f.close()
#   return page

# @app.route("/setName", methods=["POST"])
# def setName():
#   session["myName"] = request.form["name"]
#   return redirect("/")

# @app.route("/reset")
# def reset():
#   session.clear()
#   return redirect("/")

# app.run(host='0.0.0.0', port=81)

# Day 85 Challenge

from flask import Flask, request, redirect,session
from replit import db
import os

app = Flask(__name__)
# app.secret_key = os.urandom(24)
app.secret_key = os.environ['secret_key']
loggedIn = False

@app.route("/check",methods=["POST","GET"])
def check():
  info = request.form
  name = info["username"]
  try:
    if db[info["username"]]["password"] == info["password"]:
      loggedIn = True
      return redirect("/valid")
    elif db[info["username"]]["password"] != info["password"]:
      return redirect("/invalid")
  except:
  
    return redirect("/signup")
    
@app.route("/valid")
def valid():
  page = ""
  f =open("html/valid.html","r")
  page = f.read()
  f.close()
  
  if session.get("username"):
    name = session["username"]
    
  page = page.replace("{username}",name.capitalize())
    
  return page

@app.route("/invalid")
def invalid():
  page = ""
  f =open("html/invalid.html","r")
  page = f.read()
  f.close()
  return page

@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")

@app.route("/login",methods=["POST","GET"])
def login():
  try:
    info = request.form
    username= info["username"]
    password = info["password"]

    db[username] = {"password": password}
  except:
    pass
   
  page = ""
  with open("html/login.html", "r") as f:
    page = f.read() 
  f.close()
  try:
    session["username"] = request.form["username"]
    
  except:
    pass
  if session.get("username"):
     name = session["username"]
  return page

@app.route("/")
def index():
  page = ""
  f = open("html/change.html","r")
  page = f.read()
  f.close()
  return page

@app.route("/signup")
def signup():
  page = ""
  with open("index.html", "r") as f:
    page = f.read()
  f.close() 
  if session.get("username"):
    return redirect("/login")
  
  return page

app.run(host='0.0.0.0',port=81)
