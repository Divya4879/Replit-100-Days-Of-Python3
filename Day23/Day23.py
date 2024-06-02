"""
# Day 23 Code

def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

for i in range(20):
  rollDice()

"""

"""
# Fix the code

def printFavoriteColor():
  print("My favorite color is red.")

printFavoriteColor()

"""

# Day 23 Challenge
import time

print("My REPLIT LOGIN SYSTEM")

print()


def username_password_verifier():
  username = "Divya*4"
  password = "Dev&Fitness&DataAnalyticsEnthusiast"
  count = 1
  user_username = input("Enter your username: ")
  user_password = input("Enter your password: ")
  while True:
    if user_username != username and user_password != password:
      count += 1
      print("Whoops! I don't recognize the username or password you just entered. Try again!")
      user_username = input("Enter your username: ")
      user_password = input("Enter your password: ")
      if count == 5:
        time.sleep(20)
        count = 0
      
    else:
      print("""Hello Divya dear🥰🥰! Welcome back to Replit.""")
      return False
      

username_password_verifier()
