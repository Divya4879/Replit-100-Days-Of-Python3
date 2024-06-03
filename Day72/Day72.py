# Day 72 Challenge

import datetime
import hashlib
import os
import random
import time
from datetime import datetime
from getpass import getpass
from replit import db

keys = db.keys()

def colors(color):
  if color=="red":
    print("\033[31m")
  elif color=="cyan":
    print("\033[36m")
  elif color=="light_green":
    print("\033[1;32m")
  elif color=="light_purple":
    print("\033[1;35m")
  else:
    print("\033[0m")

def add_user():
  colors("light_green")
  username = input("UserName: ")
  username = f"user{username}"
  password = getpass("Password: ")
  salt = random.randint(1,1000000)
  hashed_password = f"{password}{salt}"
  hashed_password = hashlib.sha256(hashed_password.encode()).hexdigest()
  db[username] = {"password": hashed_password,"salt" : salt}
  

def login_account():
  colors("light_green")
  username = input("UserName: ")
  username = f"user{username}"
  usernames = db.prefix("user")
  if username in usernames:
    password = getpass("Password: ")
    salt = db[username]["salt"] 
    password = f"{password}{salt}"
    password = hashlib.sha256(password.encode()).hexdigest()
    
    if db[username]["password"] != password:
      colors("red")
      print("Wrong password!")
      exit()
  
    else:
      return

  else:
    colors("red")
    print("Wrong username")
    exit()

def add_entry():
  
  timestamp = datetime.now()
  colors("cyan")
  print(f"Diary entry for {timestamp}\n")
  colors("")
  diary_entry = input(""" """) 
  colors("light_purple")
  print("\nNew entry added!")
  db[f"diary{str(timestamp)}"] = diary_entry

def view_all():
  keys_entries = db.prefix("diary")
  
  keys_entries_list = list(keys_entries)
  
  count = 0

  for key in reversed(keys_entries_list):
    os.system("clear")
    counter = 0
    colors("light_purple")
    print(f"{str(key)[5:]}\n\n{db[key]}")

    counter = 1
    count += 1
    if counter == 1:
      if count == len(keys_entries):
        print()
        colors("light_purple")
        print("That's it! You're all caught up with the entries!")
        return
      print()
      colors("light_green")
      user_prompt = input("Next or exit? >> ").strip().lower()
      if user_prompt[0] == "n":  
        continue
      elif user_prompt[0] == "e":
        return

  time.sleep(2)

def view_by_date():
  keys = db.prefix("diary")
  
  colors("cyan")
  print("Viewing entries by exact date\n")
  colors("light_green")
  day = int(input("Enter Day of the entry: "))
  month = int(input("Enter month: "))
  year = int(input("Enter year: "))
  entry_date = datetime(year=year , month= month, day=day).date()
  time.sleep(1.5)
  os.system("clear")
  colors("cyan")
  print(entry_date)
  colors(" ")
  print()
  for key in reversed(keys):
    date_str = str(key)[5:].split(" ")[0]
    date_dweet = datetime.strptime(date_str, '%Y-%m-%d').date()
    if entry_date == date_dweet:
      colors("light_purple")
      print(db[key])
      time.sleep(1)
      print()
      colors(" ")
  time.sleep(2)  

def delete_entry():
  keys = db.prefix("diary")
  
  count = 1
  for key in sorted(keys, reverse=True):
    colors("light_purple")
    print(f"{count}: {db[key]}\n")
    count += 1
  colors("light_green")  
  del_seq = int(input("Choose the order of the entry you want to delete: "))

  count = 0
  while True:
    for key in sorted(keys, reverse=True):
      count += 1

      if del_seq == count: 
        del db[key]
        colors("light_purple")
        print("\nThe entry has been deleted.")
        time.sleep(1.5)
        return
      colors("red")
      print("Enter the correct sequence, in numbers!")
      continue

key = db.keys()

if len(key) == 0:
  add_user()

else:
  login_account()
  
while True:
  
  os.system("clear")
  colors("cyan")
  print("📒 Your personal Diary 📒") 
  print()

  user_choice = input("""1: Add new entry\n2: View all entries\n3: View entry by date\n4: Delete tweet\n>> """)

  colors("")
  time.sleep(0.5)
  os.system("clear")

  if user_choice == "1":
    add_entry()

  elif user_choice == "2":
    view_all()

  elif user_choice == "3":
    view_by_date()

  elif user_choice == "4":
    delete_entry()

  else:
    colors("red")
    print("Choose among options 1, 2 & 3!")
    time.sleep(2)
    continue

  time.sleep(1)  
  os.system("clear")
