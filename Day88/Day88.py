# Day 88 Code - Replit Authentication with Custom Login Button

# from flask import Flask,redirect,request

# app = Flask(__name__)

# @app.route("/hi")
# def hi():
#   if not request.headers["X-Replit-User-Id"]:
#     return redirect("/")
#   page = """<h1>{name}</h1>
#   """
#   page = page.replace("{name}",request.headers["X-Replit-User-Id"])
#   page += f"""<img src="{request.headers["X-Replit-User-Profile-Image"]}" width="200">"""
  
  
#   return page

# @app.route('/')
# def index():
#   if request.headers["X-Replit-User-Name"]:
#     return redirect("/hi")
#   page = """<html>
#   <head>
#     <title>My Website</title>
#     <script src="https://replit.com/public/js/repl-auth-v2.js"></script>
#   </head>

#   <body>
#     <h1>Here's my site</h1>
#     <p>Everyone can read this.</p>


#     <button onclick="LoginWithReplit()"> Login </button>
#   </body>  
# </html>"""
#   return page

# app.run(host='0.0.0.0', port=81)

# Day 88 Challenge

from replit import db
import os
from flask import Flask, redirect,request


app = Flask(__name__)
app.secret_key = os.environ['secret_key']
admin_userId = "16285914"

@app.route('/')
def index():

  if request.headers["X-Replit-User-Id"] == admin_userId:
    return redirect("/newEntry")
  elif request.headers["X-Replit-User-Id"] != admin_userId:
    return redirect("/wrongUser")
  
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

@app.route("/wrongUser")
def wrong_user():
  page = ""
  f = open("html/wrong.html","r")
  page = f.read()
  f.close()
  return page
  

@app.route("/newEntry",methods=["POST","GET"])
def new_entry():
  if request.headers["X-Replit-User-Id"] != admin_userId:
    return redirect("/wrongUser")
  
  page = ""
  f = open("html/new_entry.html")
  page = f.read()
  f.close()
  page = page.replace("{src}",request.headers["X-Replit-User-Profile-Image"])
  content = ""
  keys = db.prefix("entry")
  for key in reversed(list(keys)):
    content += str(db[key])
  page = page.replace("{content}",content)
  return page


@app.route("/save",methods=["POST","GET"])
def save():
  username = request.headers["X-Replit-User-Name"]
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
