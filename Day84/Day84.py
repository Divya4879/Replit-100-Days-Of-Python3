# Day 84 Challenge

from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, static_url_path='/static')

@app.route("/check",methods=["POST"])
def check():
  info = request.form
  try:
    if db[info["username"]]["password"] == info["password"]:
      return redirect("/valid")
    return redirect("/invalid")
  except:
    return redirect("/signup")

@app.route("/valid")
def valid():
  keys = db.keys()
  for key in keys:
    username = key
  page = ""
  f =open("html/valid.html","r")
  page = f.read()
  f.close()
  page = page.replace("{username}",username.capitalize())
  return page
  
@app.route("/invalid")
def invalid():
  page = ""
  f =open("html/invalid.html","r")
  page = f.read()
  f.close()
  return page


@app.route("/login",methods=["POST"])
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
  return page
  
@app.route("/")
def signup():
  return redirect("/signup")

@app.route("/signup")
def index():
  page = ""
  with open("html/index.html", "r") as f:
    page = f.read()
  f.close()  
  return page

app.run(host='0.0.0.0',port=81)
