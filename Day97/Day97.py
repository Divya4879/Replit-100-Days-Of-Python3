# Day 97 Challenge

import os,requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

textKey= os.environ['TEXT_KEY']

@app.route('/')
def index():
    page = ""
    f = open("html/index.html","r")
    page = f.read()
    f.close()

    url = "https://en.wikipedia.org/wiki/Web_development"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html,"html.parser")
    content= soup.find_all("div",{"class":"mw-content-ltr mw-parser-output"})

    text = soup.find_all("p")

    count = 0
    content = ""
    for line in text:
      if count>0:
        content += line.text
        content += "\n"
      count += 1

    payload = {
      "providers": "microsoft",
      "output_sentences": 20,
      "text": content,
      "language": "en"
    }
    headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": f"Bearer {textKey}"
    }

    url = "https://api.edenai.run/v2/text/summarize"

    response = requests.post(url, json=payload, headers=headers)

    response = response.json()
    page += """<div class="content"><h2>Summary</h2></div>"""
    page += f"""<div class="content"><i>{response["microsoft"]["result"]})</i></div>"""


    
    page += """<div class="content"><h2>References:-</h2></div>"""
    reference = soup.find_all("ol",{"class":"references"})
    count= 1
    for ref in reference:
      list_items = ref.find_all("li")
      for item in list_items:
       
        page += f"""<div class="content">{count}: {item.text.replace("^ ","")}</div>"""
        count+= 1
    
    return page

app.run(host='0.0.0.0', port=81)
