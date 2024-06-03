# Day 86 Challenge- Fully Functional Blog Engine

from replit import db
import os
from flask import Flask, redirect,request,session


app = Flask(__name__)
app.secret_key = os.environ['secret_key']

@app.route('/')
def index():
  if session.get("username"):
    return redirect("/newEntry")
  page = ""
  f = open("html/index.html","r")
  page = f.read()
  f.close()
  content = ""
  keys = db.prefix("entry")
  for key in reversed(list(keys)):
    content += str(db[key])
  page = page.replace("{content}",content)
  return page

@app.route("/login")
def login():
  if session.get("username"):
    return redirect("/newEntry")
  page = ""
  f = open("html/form.html")
  page = f.read()
  f.close()
  return page

@app.route("/check",methods=["POST"])
def check():
  if session.get("username"):
    return redirect("/newEntry")
  info = request.form
  username = info.get("username")
  password = info.get("password")

  keys = db.prefix("user")
  if len(keys) <1:
    db[f"user{username}"] = {"username":username,"password":password}
    session["username"] = password
  try:
    if db[f"user{username}"]["username"] != username or db[f"user{username}"]["password"] != password:
      db[username] != username
  except:
    page = """<head>
    <style>
       body{
       background-color:black;
       text-align:center;
       color:white;
       } 
    </style>
    </head>
    <body><h1>Enter correct credentials</h1>
    <button type="button" onclick="location.href='/login'">TRY AGAIN</button></body>
    """
    return page
  return redirect("/newEntry")

@app.route("/newEntry",methods=["POST","GET"])
def new_entry():
  page = ""
  f = open("html/new_entry.html")
  page = f.read()
  f.close()
  content = ""
  keys = db.prefix("entry")
  for key in reversed(list(keys)):
    content += str(db[key])
  page = page.replace("{content}",content)
  return page

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

@app.route("/save",methods=["POST","GET"])
def save():
  content = request.form
  
  title = content["title"]
  date = content.get("date")
  blog = content.get("blog")

  page = ""
  f = open("html/blog.html","r")
  page = f.read()
  f.close()
  
  page= page.replace("{title}",title)
  page= page.replace("{date}",str(date))
  page= page.replace("{blog}",str(blog))
  db[f"entry{title}"] = page
  
  return redirect("/newEntry")

app.run(host='0.0.0.0', port=81)
