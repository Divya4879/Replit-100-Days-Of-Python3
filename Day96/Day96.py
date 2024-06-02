# Day 96 Challenge

import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    page = ""
    f = open("html/index.html","r")
    page = f.read()
    f.close()
    
    url = "https://news.ycombinator.com/newest"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html,"html.parser")

    links = soup.find_all("a",{"rel":"nofollow"})

    things = ["python","replit","technology","programming","company","ai"]
    
    
    for counter,link in enumerate(links):
      if counter>2:
       text = link.text
       textList = text.split()
       containsWord = False
       for word in textList:
         if word.lower() in things:
           containsWord= True
     
       if containsWord:
         page += f"""<div class="content"><i>{link.text}</i><br>
         <a href="{link["href"]}">{link["href"]}</a></div>"""

    return page

app.run(host='0.0.0.0', port=81)
