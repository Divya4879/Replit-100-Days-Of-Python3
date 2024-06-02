import requests, json, os
from flask import Flask

app = Flask(__name__)

news_key = os.environ['NEWS_KEY']
text_key = os.environ['TEXT_KEY']

country = "in"

@app.route("/news")
def news():
  page = ""
  f  = open("template/html/news.html","r")
  page = f.read()
  f.close()
  url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_key}"

  response = requests.get(url)

  def get_news():
    i = 0
    news = {}
    while i < 5:
      for article in response.json()["articles"]:
        value = article["content"]
        if value != None:
          news[i] = value
          i += 1
        if i == 5:
          return news

  news = get_news()
  res = ""
  
  for i in news:
    url = f"https://api.textgears.com/summarize?key={text_key}&language=en-GB&text={news[i]}"
    response = requests.get(url)
    response = response.json()
    summary = response.get("response", {}).get("summary", "")
    response,extra = summary.split("...", 1) if "..." in summary else (summary, "")
    res += response[0]
    res += "<br><br><br>"
  page = page.replace("{news}",res)
  return page

@app.route('/')
def index():
  page = ""
  f  = open("template/html/index.html","r")
  page = f.read()
  f.close()
  
  return page


app.run(host='0.0.0.0', port=81)
