# Day 98 CHALLENGE

import os,requests,random
import time,schedule,smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

password = os.environ['ACCOUNT_KEY']
username = os.environ['username']

url = "https://www.usatoday.com/story/life/2023/11/30/positive-quotes-to-inspire/11359498002"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,"html.parser")

content = soup.find_all("li",{"class":"gnt_ar_b_ul_li"})

quotes = []

for line in content:
  quotes.append(line.text)

def send_mail():
  random_quote = random.choice(quotes)
  email = random_quote
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 
  msg = MIMEMultipart() 
  msg['To'] = username 
  msg['From'] = username 
  msg['Subject'] = "Your Daily Quota of Motivation" 
  msg.attach(MIMEText(email, 'html'))
  
  s.send_message(msg) 
  del msg 

def sendMessage():
  print("Sending a little Positivity")
  send_mail()

schedule.every(24).hours.do(sendMessage)

while True:
  schedule.run_pending()
  time.sleep(4)
