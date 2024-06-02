# Day 91 Challenge

from replit import db
import requests,time,os

def new_joke():
  joke = requests.get("https://icanhazdadjoke.com/",headers={"Accept": "application/json"})

  joke = joke.json()
  print()
  global dad_joke,joke_id
  dad_joke = joke['joke']
  joke_id = joke['id']
  return id,dad_joke
  
def save_joke():
  db[joke_id] = dad_joke
  print("\nSAVED")
  time.sleep(2)
  os.system("clear")

def load_all():
  keys = db.keys()
  for key in keys:
    print(db[key])
    time.sleep(1)
    print()
  time.sleep(2)
  os.system("clear")

print("A Dad Joke's Program for a happier you!🤣🤣")

while True:
  
  choice = input("""\nHello! Do you want to:-\n\n1: Get a new joke?\n2: Save the joke\n3: Load all your jokes?\n\n>>""")
 
  if choice == "1":
    new_joke()
    print(dad_joke)
  
  elif choice == "2":
    save_joke()
  
  elif choice == "3":
    load_all()
  
  else:
    print("Choose from options 1, 2 & 3")
