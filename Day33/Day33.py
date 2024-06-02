"""
# Day 33 Code

myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()


myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"The {item} is not in your list.")
  printList()


# Fix the Code
myPartyList = []

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()

"""

# Day 33 Challenge
import os,time

def colored_text(color,word):
  if color=="red":
    print("\033[31m", word, sep="", end=" ")
  elif color=="green":
    print("\033[32m", word, sep="", end=" ")
  elif color=="purple":
    print("\033[35m", word, sep="", end=" ")
  elif color=="yellow":
    print("\033[1;33m", word, sep="", end=" ")
  else:
    print("\033[0m", word, sep="", end=" ")


toDoList = []

colored_text("yellow","")
print("  WELCOME TO YOUR TO-DO LIST MANAGER📋",end ="\n\n")
colored_text("white","")
def add_item():
  task = input("What do you want to add in your list? ")
  time.sleep(0.5)
  print()
  toDoList.append(task)
  colored_text("purple","")
  print(f"{task} is added in your To-Do list")
  time.sleep(1)
  view_list()
  
  
def remove_item():
  task = input("Which task have you completed and want to remove from your list? ")
  time.sleep(0.5)
  print()
  if task in toDoList:
    toDoList.remove(task)
    colored_text("purple","")
    print(f"Congratulations🥳,{task} has been completed & removed from your to-do list!")
    time.sleep(1)
    view_list()
  else:
    colored_text("red","")
    print(f"{task} wasn't in your To-Do List!")
    print("Try again!\n")
    time.sleep(1)
    os.system("clear")
    colored_text("white","")
    
    

def view_list():
  os.system("clear")
  colored_text("green","")
  title = "T0-DO LIST"
  print(f"{title : ^40}",end="\n\n")
  for task in toDoList:
    print(f"{task : ^44}")
  colored_text("white","")
  print()

while True: 
  user_prompt = input("Do you want to view your list, add an item to it, or edit the list(remove a task already completed)? ")
  time.sleep(0.5)
  print()
  
  if user_prompt == "add":
    add_item()
  
  elif user_prompt == "remove" or user_prompt == "edit":
    remove_item()

  elif user_prompt == "view":
    view_list()
  
  elif user_prompt == "exit":
    print("Goodbye✌! You have exited the program and the list you created is forever lost!")
    time.sleep(2)
    os.system("clear")
    quit()
  
  else:
    colored_text("red","")
    print("I didn't get that. Try again.")
    colored_text("white","")
    print()
