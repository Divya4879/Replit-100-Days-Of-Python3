# Day 70 Code

# import os
# adminPassword = os.environ['password']
# # Uses the os library to talk to the environment and get the secret password stored there.

# password = input("Password>> ")
# if password == adminPassword:
#   print("Hello dear Divya!")

# else:
#   print("Who are you??")

# Fix My Code

"""

import os
from getpass import getpass

password = os.environ['password'] 

userPass = getpass("Password > ")

if userPass == password:
  print("Well done")
else:
  print("Better luck next time")
  
"""

# Day 70 Challenge

import os
from getpass import getpass

print("🌟Login System🌟\n")

adminUsername =  os.environ['username']
adminPassword = os.environ['password']

username = getpass("Username: ")
password = getpass("Password: ")

if username == adminUsername:
  if password != adminPassword:
    print("Nice try! But you aren't me 😏")
    exit()

  print(f"Welcome back {adminUsername} dear🫧💗✨❣️")
  exit()

print(f"Hello {username}! Wish you a great day ahead ˚˖𓍢ִ໋🌷͙֒✧˚.🎀༘⋆")
