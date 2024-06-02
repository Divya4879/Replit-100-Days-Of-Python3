import requests, os,json
from flask import Flask
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

news_key = os.environ['NEWS_KEY']
image_key = os.environ['IMAGE_KEY']
video_key = os.environ['VIDEO_KEY']

country = "in"

@app.route("/songs")
def songs():
  page = ""
  f  = open("songs.html","r")
  page = f.read()
  f.close()
  url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={news_key}"

  response = requests.get(url)
  
  def get_news():
    i = 0
    news = {}

    
    while i < 5:
      for article in response.json()["articles"]:
        value = article["content"]
        title = article["title"]
        news[i] = [value,title]
        
        i += 1
        if i == 5:
          return news

  news = get_news()
  res = ""
  
  for i in news:

    res += f"{news[i][1]}"
    res+= "<br><br>"
    clientID = os.environ['CLIENT_ID']
    clientSECRET = os.environ['CLIENT_SECRET']

    url = "https://accounts.spotify.com/api/token"
    data = { "grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSECRET)

    response = requests.post(url, data=data, auth=auth)
    accessToken = response.json()["access_token"]
    headers = {"Authorization" : f"Bearer {accessToken}"}

    headline = f"{news[i][0]}".replace(" ", "%20")
    
    url = "https://api.spotify.com/v1/search"
    search = f"?q={headline}&type=track&limit=1"
    fullURL = f"{url}{search}"
    response = requests.get(fullURL, headers=headers)
    data = response.json()
    for track in data["tracks"]["items"]:
      global link
      
      link = track["album"]["artists"][0]["external_urls"]["spotify"]
      res += f"""<a href="{link}">{link}</a>"""
    res+= "<br>"
    
    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
      files = {
          'prompt': (None, news[i][1], 'text/plain')
      },
      headers = { 'x-api-key': image_key}
    )
    if (r.ok):
      f = open(f"image{i}.jpg","wb")
      f.write(r.content)
      f.close()
      
      res+= "<br>"
      
    else:
      r.raise_for_status()
   
    res += "<br><br><br>"
  page = page.replace("{news}",res)
  return page

@app.route('/')
def index():
  page = ""
  f  = open("index.html","r")
  page = f.read()
  f.close()

  return page

app.run(host='0.0.0.0', port=81)
