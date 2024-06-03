# Day 61 Code

# from replit import db

# db["test"] = "Good Day!"
# value = db["test"]
# print(value)


# del db["test"]
# value = db["test"]
# print(value)

# db["user1"] = "Divya"
# db["user2"] = "Riya"
# db["user3"] = "Divyam"
# db["user4"] = "Piya"
# db["user5"] = "Divyangini"

# keys = db.prefix("user")
# print(keys)


# # keys = db.keys()
# for key in keys:
#   print(f"{key}: {db[key]}")
#   del db[key]

# keys = db.keys()
# for key in keys:
#   print(key)
#   del db[key]

# db["divya"] = {"username": "Divya", "password": "GoodDay"}  

# value = db["divya"]
# password = value["password"]
# print(password)

# keys = db.keys()
# for key in keys:
#   print(f"""{key}: {db[key]}""")

# try:
#   value = db["key"]
# except:
#   pass

# Fix The Code

# from replit import db

# keys = db.keys()

# for key in keys:
#   print(f"{key}: {db[key]}")
#   del db[key]

# Day 61 Challenge

from replit import db 
import os,time,datetime

def add_dweet():
  tweet = input("🐇: ")
  timestamp = datetime.datetime.now()
  db[str(timestamp)] = tweet
  time.sleep(0.5)

def view_dweets():
  keys = db.keys()
  counter = 0
  while True: 
    for key in reversed(sorted(keys)):
      print(db[key])
      counter += 1
      
      if counter == len(keys)-1:
        print()
        print("That's all the dweets you've posted till now!")
        time.sleep(3)
        return
      if counter %10 == 0:
        print()
        user_prompt = input("Wanna see 10 more dweets? (y/n): ").strip().lower()
        print()
        if user_prompt[0] == "y":
          continue
      
        elif user_prompt[0] == "n":
          return

def delete_dweet():
  keys = db.keys()
  counter = 1
  for key in reversed(sorted(keys)):
    print(f"{counter}: {db[key]}")
    counter += 1

  print()
  dweet = input("Which dweet do you want to delete?(enter the numeric order) >> ")
  
  counter = 0
  for key in reversed(sorted(keys)):
    counter += 1
    if counter == int(dweet):
      print(counter)
      del db[key]
  time.sleep(3)
    
while True:
  os.system("clear")
  print("Dweeter 🐇🐇")
  print()

  user_choice = input("1: Add Dweet\n2: View Dweet\n3: Delete a Dweet\n>> ")
  time.sleep(1)
  os.system("clear")
  if user_choice == "1":
    add_dweet()

  elif user_choice == "2":
    view_dweets()
    
  elif user_choice == "3":
    delete_dweet()
    
  else:
    print("Choose option 1 or 2 or 3 and try again!") 
