# Day 36 Code
"""
name = input("What's your name? ")
if name.lower().strip() == "divya": 
  print("Hello Dear!")
else: 
  print("Ciao!")
  

myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").strip().capitalize()
  if addItem not in myList:
    myList.append(addItem) 
  printList()


# Fix The Code

whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip().lower() == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.upper() == "TACOS":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")

"""

# Day 36 Challenge
import os,time

names_list = []

def view_list():
  print()
  for index in range(len(names_list)):
    print(names_list[index])

  time.sleep(10)
  os.system("clear")

while True:
  first_name = input("Enter a person's first name: ").strip().capitalize()
  
  last_name = input("Enter their surname: ").strip().capitalize()

  name = f"{first_name} {last_name}"
  names_list.append(name)
  view_list()
