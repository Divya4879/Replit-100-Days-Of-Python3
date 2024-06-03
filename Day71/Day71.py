# Day 71 - Hashing & Salting

# from replit import db
# import random

# username = "Divya"
# password = "divyanka"
# salt = 1289
# password = hash(f"{password}{salt}")

# db[username] = {"password" :password,"salt":salt}


# userUserName = input("Username: ")

# usernames = db.keys()

# for username in usernames:

#   if username == userUserName:
#     userPassword = input("Password: ")
#     salt = db[username]["salt"]

#     userPassword = hash(f"{userPassword}{salt}")


#     if userPassword == db[username]["password"]:
#       print("You're successfully logged in!")

#     else:
#       print("Try again!")
#       exit()
  
#   else:
#       print("User doesn't exist")

# Fix the code

# from replit import db

# ans = input("Password >") 
# salt = db["david"]["salt"] 
# newPassword = f"{ans}{salt}"
# newPassword = hash(newPassword) 

# if newPassword == db["david"]["password"]: 
#   print("Login successful")

# Day 71 Challenge

import os
import random
import time
from getpass import getpass
from replit import db


def new_user():
  time.sleep(1.5)
  os.system("clear")
  username = input("Username: ")
  usernames = db.keys()
  if username not in usernames:
    password = getpass("Password: ")
    salt = random.randint(1000,9999)
    hashed_password = f"{password}{salt}"
    hashed_password = hash(hashed_password)
    
    db[username] = {"password":
  hashed_password,"salt":salt}
    
    print(f"\n{username} successfully added.")
    return

  print("This user already exists!!")
  user_prompt = input("Want to log in to your account? (y/n) >> ").strip().lower()[0]
  
  if user_prompt == "y":
    login_account()

def login_account():
  time.sleep(1.5)
  os.system("clear")
  
  username = input("Username: ")
  usernames = db.keys()
  
  if username not in usernames:
    print(f"{username} hasn't created an account yet!")
    user_prompt = input("Want to create an account instead? (y/n) ").strip().lower()[0]
    if user_prompt == "y":
      new_user()
    return
     
  user_password = getpass("Password: ")
  salt = db[username]["salt"]

  user_password = f"{user_password}{salt}"
  user_password = hash(user_password)
  
  if db[username]["password"] == user_password:
    
    print(f"Welcome back {username}!\nYou're logged in.")
    return
  
  print("Wrong password entered!!")
  
while True:  
  time.sleep(1.5)
  os.system("clear")
  
  print("🌟 Login System 🌟\n")
  user_choice = input("1: New User\n2: Login\n3: View all Usernames\n4: Exit\n>> ")
  
  if user_choice == "1":
    new_user()
  
  elif user_choice == "2":
    login_account()
    
  elif user_choice == "3":
    usernames = db.keys()
    for username in usernames:
      print(username)

  elif user_choice == "4":
    exit()
