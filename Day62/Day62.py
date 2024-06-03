# Day 62 Challenge

import time, os, datetime
from replit import db 

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


def add_entry():
  timestamp = datetime.datetime.now()
  colors("cyan")
  print(f"Diary entry for {timestamp}\n")
  colors("")
  diary_entry = input() 
  colors("light_purple")
  print("\nNew entry added!")
  db[timestamp] = diary_entry

def view_all():
  keys_entries = db.keys() 
  count = 0
  
  for key in sorted(keys_entries, reverse=True):
    os.system("clear")
    counter = 0
    colors("light_purple")
    print(f"{key}\n\n{db[key]}")
    
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
  keys = db.keys()
  colors("cyan")
  print("Viewing entries by exact date\n")
  colors("light_green")
  day = int(input("Enter Day of the entry: "))
  month = int(input("Enter month: "))
  year = int(input("Enter year: "))
  entry_date = datetime.date(year , month , day)
  time.sleep(1.5)
  os.system("clear")
  colors("cyan")
  print(entry_date)
  colors(" ")
  print()
  for key in keys:
    date_str = str(key).split(" ")[0]
    date_dweet = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    if entry_date == date_dweet:
      colors("light_purple")
      print(db[key])
      time.sleep(1)
      print()
      colors(" ")
  time.sleep(2)  

def delete_tweet():
  keys = db.keys()
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

# my_password = "YouAreMe,akaDivya,right?"
my_username = "Divya"
my_password = "c"

colors("light_green")

username = input("UserName: ")
password = input("Password: ")

if my_username!= username or password != my_password:
  colors("red")
  print("Don't try to look through other's diaries!")
  
  exit()

while True:
  os.system("clear")
  colors("cyan")
  print("📒 Your personal Diary 📒") 
  print()
  
  user_choice = input("1: Add new entry\n2: View all entries\n3: View entry by date\n4: Delete tweet\n>> ")
  
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
    delete_tweet()
  
  else:
    colors("red")
    print("Choose among options 1, 2 & 3!")
    time.sleep(2)
    continue

  time.sleep(1)  
  os.system("clear")
