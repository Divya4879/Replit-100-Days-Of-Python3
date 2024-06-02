# Day 100 Challenge

import os,requests,random
import time,schedule,smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from replit import db

password = os.environ['ACCOUNT_KEY']
username = os.environ['USERNAME']

def site_scrape():
  url = "https://www.penguinrandomhouse.com/books/555887/the-winters-tale-by-william-shakespeare"
  
  response = requests.get(url)
  html = response.text
  
  soup = BeautifulSoup(html,"html.parser")
  
  content = soup.find_all("div",{"class":"title-price-container"})
  
  priceList= content[0].text
  priceList = priceList.replace("\n","").split(" ")
  
  price = priceList[len(priceList)-2].replace("$","")
  price = int(price.replace(".00",""))
  
  name = soup.find("h1")

  try:
    db["name"] = {"desired_price": 10.2}
    db["price"] = price
  except:
    pass
  return url,name,price

def send_mail():
  url,name,price=site_scrape()
  email = f"""<p style='font-size:20px; color:black;'><a href="{url}">{name}</a>book is now available at ${price}, which is lower than your desired price of ${db['name']['desired_price']}.</p>"""
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 
  msg = MIMEMultipart() 
  msg['To'] = username 
  msg['From'] = username 
  msg['Subject'] = "Price Reduction in your fav book" 
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 

def sendMessage():
  print("Sending a little Positivity💖💗🥰💞")
  send_mail()

sendMessage()

schedule.every(24).hours.do(sendMessage)

while True:
  if db["price"] <= db["name"]["desired_price"]:  
    schedule.run_pending()
    time.sleep(4)
