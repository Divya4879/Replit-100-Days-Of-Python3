# DAY 93 CHALLENGE

import requests, os
from flask import Flask,request
from requests.auth import HTTPBasicAuth
from replit import db
# keys = db.keys()
# for key in keys:
#   print(key)
#   print(db[key])
#   print()
#   del db[key]
app = Flask(__name__)

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)

accessToken = response.json()["access_token"]

url = "https://api.spotify.com/v1/search"

headers = {'Authorization': f'Bearer {accessToken}'}

@app.route("/more",methods=["POST","GET"])
def more():
  
  offset = db[yr] 
  if offset >200:
    db[yr] = 0
  else:
    db[yr] += 10
  offset = db[yr]
  print(offset, type(offset))
  search = f"?q=year%3A{yr}&type=track&limit=10&offset={offset}"

  fullURL = f"{url}{search}"

  response = requests.get(fullURL, headers=headers)

  tracks = ""
  data = response.json()

  for track in data["tracks"]["items"]:
    global name,link
    name = track["name"]
    link = track["preview_url"]
    tracks += f"""<hr><h1 style="font-size:30px">{name}</h1>
    <audio controls>
      <source src="{link}" type="audio/mpeg">
    </audio>"""

  page = ""
  f = open("template/html/index.html","r")
  page = f.read()
  f.close()

  page = page.replace("{song_tracks}",tracks)

  page= page.replace("{bg-img}","https://media2.giphy.com/media/1pmatQ3LcP5XFYxSWF/giphy.webp?cid=790b7611ofnkwaz6uhxh34a5etykycex2288owypfofd6kci&ep=v1_gifs_search&rid=giphy.webp&ct=g.gif")
  more = """<hr><button type="submit" id="btn" onclick = "location.href='/more'">More</button>"""

  page = page.replace("{more}",more)

  return page

@app.route("/search",methods=["POST","GET"])
def search():
  
  global yr,offset
  yr = request.form["yr"].strip()
  offset = 0
  db[yr] = offset
  
  search = f"?q=year%3A{yr}&type=track&limit=10&offset={offset}"
    
  fullURL = f"{url}{search}"
  
  response = requests.get(fullURL, headers=headers)

  tracks = ""
  data = response.json()
  
  for track in data["tracks"]["items"]:
    global name,link
    name = track["name"]
    link = track["preview_url"]
    tracks += f"""<hr><h1 style="font-size:30px">{name}</h1>
    <audio controls>
      <source src="{link}" type="audio/mpeg">
    </audio>"""
    
  page = ""
  f = open("template/html/index.html","r")
  page = f.read()
  f.close()
  
  page = page.replace("{song_tracks}",tracks)
  
  page= page.replace("{bg-img}","https://media2.giphy.com/media/1pmatQ3LcP5XFYxSWF/giphy.webp?cid=790b7611ofnkwaz6uhxh34a5etykycex2288owypfofd6kci&ep=v1_gifs_search&rid=giphy.webp&ct=g.gif")
  more = """<hr><button type="submit" id="btn" onclick = "location.href='/more'">More</button>"""
  
  page = page.replace("{more}",more)

  return page

@app.route("/")
def index():
  page = ""
  f = open("template/html/index.html","r")
  page = f.read()
  f.close()
  try:
    query  = request.form["yr"]
  except:
    page = page.replace("{song_tracks}","")
    page= page.replace("{bg-img}","https://images.unsplash.com/photo-1553649084-3e42773ff0e3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fG11c2ljJTIwd2FsbHBhcGVyfGVufDB8fDB8fHww")
    page = page.replace("{more}","")

  return page

app.run(host='0.0.0.0', port=81)
