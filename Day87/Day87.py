# Day 87 code - Replit Authentication

# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#   username = request.headers["X-Replit-User-Name"]
#   return f"Hello {username}"

# app.run(host='0.0.0.0', port=81)

# Day 87 Challenge

from replit import db
import os
from flask import Flask, redirect,request,session


app = Flask(__name__)
app.secret_key = os.environ['secret_key']

@app.route('/')
def index():
  
  if session.get("username") == "divyaDevPython":
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

@app.route("/newEntry",methods=["POST","GET"])
def new_entry():
  username = request.headers["X-Replit-User-Name"]
  
  session["username"] = username
  if username != "divyaDevPython":
    return redirect("/")

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
  username = request.headers["X-Replit-User-Name"]

  session["username"] = username
  if username != "divyaDevPython":
    return redirect("/")
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
