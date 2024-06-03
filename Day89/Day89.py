# Day 89 Challenge

from flask import Flask,redirect,request
import datetime, os
from replit import db

app = Flask(__name__)
app.secret_key = os.environ['secret_key']

timestamp_key = datetime.datetime.now()

@app.route("/send",methods=["POST","GET"])
def send():
  info = request.form
  timestamp = str(datetime.datetime.now())
  timestamp = timestamp.replace(" ","")
  timestamp = timestamp.replace("-","")
  timestamp = timestamp.replace(":","")
  db["name"] = request.headers["X-Replit-User-Name"]
  db["src"] = request.headers["X-Replit-User-Profile-Image"]
  db["datetime"] = timestamp
  db["message"] = info["message"]
  page = ""
  f = open("html/msg.html","r")
  page = f.read()
  f.close()
  page = page.replace("{name}",db["name"])
  page = page.replace("{src}",db["src"])
  page = page.replace("{datetime}",db["datetime"])
  page = page.replace("{msg}",db["message"])
  
  del db["name"]
  del db["src"]
  del db["datetime"]
  del db["message"]
  
  db[f"msg{timestamp}"] = page
  return redirect("/user")

@app.route("/delete",methods=["POST","GET"])
def delete():
  name = request.form   
  id = name["postID"] 
  del db[id]
  
  return redirect("/admin")
  
  
@app.route("/admin")
def admin():
  page = ""
  f = open("html/admin.html","r")
  page = f.read()
  f.close()
  page= page.replace("{name}",request.headers["X-Replit-User-Name"])
  page= page.replace("{src}",request.headers["X-Replit-User-Profile-Image"])
  content = ""
  keys = db.prefix("msg")

  for key in keys[-1:-6:-1]:
    content += db[key]
    content += """
    <form method="post" action="/delete"><button  type="submit" 
    onclick="location.href='/delete'" 
    name="postID" value="{key}">Delete</button><hr><hr>
    </form>
  """
    
    content = content.replace("{key}",key)
  page = page.replace("{content}",content)
    
  return page

@app.route("/user",methods = ["POST","GET"])
def user():
  page = ""
  f = open("html/chat.html","r")
  page = f.read()
  f.close()
  page= page.replace("{name}",request.headers["X-Replit-User-Name"])
  page= page.replace("{src}",request.headers["X-Replit-User-Profile-Image"])
 
  content = ""
  keys = db.prefix("msg")
  for key in keys[-1:-6:-1]:
    content += db[key]
  page = page.replace("{content}",content)
  if request.headers["X-Replit-User-Id"] == "16285914":
    page += """<button type="submit" onclick="location.href='/admin'">Admin</button>"""
  return page

@app.route('/')
def index():
    if request.headers["X-Replit-User-Id"]:
      return redirect("/user")

    page = ""
    f = open("html/index.html","r")
    page = f.read()
    f.close()
    
    return page
  
app.run(host='0.0.0.0', port=81)
