# Day 78 Challenge

from flask import Flask,redirect
import datetime

app = Flask(__name__)

remarks = {
    "78": "Super excited for all the learning so far & the upcoming projects.",
    "79": "Seems easy, coz I've worked with it earlier!",
    "80": "Looking forward to the backend stuff!",
    "81": "Looking forward to this challenge",
    "82": "Seems like a better approach used than the previous day.",
    "83": "Woah, custom blogs! Let's see what it's about!",
    "84": "Afraid, excited, proud, nostalgic!",
    "85": "Converting into stateful?",
    "86": "Woah, a fully-functioning blog!",
    "87": "It's like DSA, start with brute method, to optimized solutions!",
    "88": "Dunno what it's exactly, but it's great!",
    "89": "Woah! A great project!",
    "90": "I know a teeny-tiny bit of JSON already!Hope it's not too hard.",
    "91": "Excited for the dad jokes!",
    "92": "My own weather app!",
    "93": "Seems hard, but still excited for it!",
    "94": "Mashup Party, ok no, a website!",
    "95": "Tracking- another great project!",
    "96": "Absolutely exciting/important stuff, I'm itching to do it!",
    "97": "Summarize it all- A great journey so far...",
    "98": "Automation: Let's see what it's about.",
    "99": "Just 1 more day + a great & hard project",
    "100": "Finally, I'm done with a bang!!!"
}

@app.route('/<dayNumber>')
def index(dayNumber):
  
  f = open("template/html/dayReflection.html","r")
  page = f.read()
  page = page.replace("{dayNumber}",dayNumber)
  reflection = ""
  for i in remarks:
    if i == dayNumber:
      reflection = remarks[i]
      
  page = page.replace("{reflection}",reflection)
  f.close()
  return page

app.run(host='0.0.0.0', port=81)
