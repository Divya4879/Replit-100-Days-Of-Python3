# Day 99 Challenge

import os,requests,random
import time,schedule,smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from replit import db

password = os.environ['ACCOUNT_KEY']
username = os.environ['USERNAME']

url = "https://dev.events/ON/tech"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,"html.parser")

content = soup.find_all("a",{"class":"has-text-dark is-uppercase"})


interests = ["global","code","frontend","python","tech","software"]

counter = 0
for i in content:
  eventsList = i.text.split(" ")
  for keyword in eventsList:
    event = i.text
    
    if keyword.lower() in interests:
      if counter > 2:
        link = f"https://dev.events/{i.get('href')}"
        # db[str(event)] = link
      else:
        link= i.get('href')
        # db[str(event)] = link

  counter += 1

def send_mail():
  email = ""
  keys = db.keys()
  # for key in keys:
  #   email += f"""<a href="{db[key]}">{key}</a><br>"""
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 
   
  if event not in keys:
    email = f"""<a href="{link}">{event}</a><br>"""
    db[str(event)] = link
    print("New exciting events reminder mail coming up!")
    del msg
  else:
    print("No new events in the past 6 hours.")
    return
    
  msg = MIMEMultipart()
  msg['To'] = username 
  msg['From'] = username 
  msg['Subject'] = "Exciting Tech Events Updates" 
  msg.attach(MIMEText(email, 'html'))
  s.send_message(msg) 
  del msg 

def sendMessage():
  
  send_mail()
sendMessage()

schedule.every(6).hours.do(sendMessage)

while True:
  schedule.run_pending()
  time.sleep(4)
