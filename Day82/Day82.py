# DAY 82 CODE

# from flask import Flask,request,redirect

# app = Flask(__name__)


# @app.route('/', methods=["GET"])
# def index():
#   get =  request.args
#   if get["divya"] == "Python":
#     return "Hello 🐍"
#   return("Hello 💗")
# app.run(host='0.0.0.0', port=81)

# Day 82 Challenge

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("/language")

@app.route("/language", methods=["GET"])
def choice():
  get = request.args
  if get == {}:
    content = ""
    with open("template/html/eng.html", "r") as f:
      content = f.read()
    f.close()
    return content
  
  elif get["lang"].lower() == "hin":
    content = ""
    with open("template/html/hindi.html", "r") as f:
      content = f.read()
    f.close()
    return content

  elif get["lang"].lower() == "jap":
    content = ""
    with open("template/html/japanese.html", "r") as f:
      content = f.read()
    f.close()
    return content

  elif get["lang"].lower() == "italian":
    content = ""
    with open("template/html/italian.html", "r") as f:
      content = f.read()
    f.close()
    return content

  else:
    content = ""
    with open("template/html/eng.html", "r") as f:
      content = f.read()
    f.close()
    return content
   
  
app.run(host='0.0.0.0', port=81)
