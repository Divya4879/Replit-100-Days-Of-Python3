# Day 50 Challenge

import random, os,time

def add_idea():
  new_idea = input("Input your idea >> ")
  print()
  print("Nice! Your idea has been stored.")
  f.write(f"{new_idea}\n")

def view_idea():
  f = open("my.ideas","r")
  ideas = f.read().split("\n")

  random_idea = ideas[random.randint(0,len(ideas)-2)]

  print(f"Random Idea: {random_idea}")

while True:
  f = open("my.ideas","a+")
  os.system("clear")
  
  print("🌟Idea Storage🌟")
  print()
  print("""1. Add an idea
2. Load up a random idea
  """)
  
  user_prompt = input(">> ")
  os.system("clear")
  print()
  if user_prompt == "1":
    add_idea()
    
  elif user_prompt == "2":
    g = open("my.ideas","r")
    view_idea()
       
  time.sleep(1)
  f.close()
