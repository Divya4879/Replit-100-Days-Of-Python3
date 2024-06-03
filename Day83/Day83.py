# Day 83 CHALLENGE - My blogging website, with customized themes

from flask import Flask,redirect,request
import datetime

app = Flask(__name__,static_url_path="/static")

@app.route("/")
def redirReplit():
    return redirect("/python")


@app.route('/python',methods=["PUT","GET"])
def python_review():
  dateToday = datetime.date.today()
  author = "Divya"
  src = "static/images/download (1).jpg"
  profile = "static/images/download.jpg"
  page = ""
  content = """I'm Divya, and just wanted to share my feedback on this challenge so far. Firstly, lemme give my background. I'm a CSE major (B-Tech). I liked Python immensely, when I first started it, and hence I'm doing this challenge to enhance my Python skills, coding skills, build a new project every single day, the great community, the bite-sized content of a day's lecture.<br><br>I've loved it so far, but of course, I've a suggestion/request/feedback to have consistency in the written code and the videos. I prefer reading to watching, and many times, due to inconsistency between what's written as a Day's challenge requirements & what's on the video, I've had to remake my project by more than half."""
  f = open("template/blog.html","r")
  page = f.read()
  f.close()
  page = page.replace("{heading}","Python Challenge Review")
  page = page.replace("{date}",str(dateToday))
  page = page.replace("{content}",content)
  page = page.replace("{author}",author)
  page = page.replace("{src}",src)
  page = page.replace("{content}",content)
  page = page.replace("{profile}",profile)
  get = request.args
  if get == {} or get["theme"] == "default":
    return page

  
  elif get["theme"] == "dark":
    f = open("template/dark.html","r")
    page = f.read()
    f.close()
    page = page.replace("{heading}","Python Challenge Review")
    page = page.replace("{date}",str(dateToday))
    page = page.replace("{content}",content)
    page = page.replace("{author}",author)
    page = page.replace("{src}",src)
    page = page.replace("{content}",content)
    page = page.replace("{profile}",profile)
    return page

 
  elif get["theme"] == "starry":
    f = open("template/fancy.html","r")
    page = f.read()
    f.close()
    page = page.replace("{heading}","Python Challenge Review")
    page = page.replace("{date}",str(dateToday))
    page = page.replace("{content}",content)
    page = page.replace("{author}",author)
    page = page.replace("{src}",src)
    page = page.replace("{content}",content)
    page = page.replace("{profile}",profile)
    return page
    
  return page  
  

app.run(host='0.0.0.0', port=81)
