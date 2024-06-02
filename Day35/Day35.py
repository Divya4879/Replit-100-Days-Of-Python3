# Day 35 Challenge
import os,time

def colored_text(color,word):
  if color=="red":
    print("\033[31m", word, sep="", end=" ")
  elif color=="blue":
    print("\033[34m", word, sep="", end=" ")
  elif color=="green":
    print("\033[32m", word, sep="", end=" ")
  elif color=="purple":
    print("\033[35m", word, sep="", end=" ")
  elif color=="yellow":
    print("\033[1;33m", word, sep="", end=" ")
  else:
    print("\033[0m", word, sep="", end=" ")


toDoList = []

def add_item():
  task = input("What do you want to add in your list? ")
  if task in toDoList:
    colored_text("blue","")
    print(f"{task} is already in your agenda for today.")
    time.sleep(1)
    
  else:
    
    time.sleep(0.5)
    print()
    toDoList.append(task)
    colored_text("purple","")
    print(f"{task} is added in your To-Do list")
    time.sleep(0.5)
    view_list()
    time.sleep(0.5)
 

def edit_task():
  task = input("Which task from your agenda do you want to edit? ")
  if task in toDoList:
    index = toDoList.index(task)
    toDoList[index] = input("")
    colored_text("purple","")
    print(f"{task} is edited to {toDoList[index]}")   
    time.sleep(1)
  else:
    colored_text("red","")
    print(f"{task} wasn't in your list.")
    time.sleep(1)
  
def remove_item():
  task = input("Which task do you want to remove from your list? ")
  time.sleep(0.5)
  print()
  if task in toDoList:
    user_query = input("Is this the item they you want to remove? ")
    if user_query == "yes":   
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
    colored_text("white","")

def view_list():
  os.system("clear")
  colored_text("green","")
  title = "T0-DO LIST"
  print(f"{title : ^40}",end="\n\n")

  for task in toDoList:
    print(f"{      task : ^42}")
  colored_text("white","")
  print()
  
while True:
  os.system("clear")
  colored_text("yellow","")
  print("TO-DO LIST MANAGER 📋")
  
  user_prompt = input("\n1. Add a task\n2. Edit a task\n3. Remove an item from your list\n4. View your list\n5. Create a new list\n6. Quit this application\n>> ")
  colored_text("white","")
  time.sleep(0.5)
  print()
    
  if user_prompt == "1":
    add_item()
    
  elif user_prompt == "2":
    edit_task()
    time.sleep(1) 
    
  elif user_prompt == "3":
    remove_item()

  elif user_prompt == "4":
    view_list()
    time.sleep(4)

  elif user_prompt == "5":
    toDoList = []
    print("You can create a brand new list now.")
    time.sleep(1)

  elif user_prompt == "6":
    print("Goodbye✌! You have exited the program and the list you created is forever lost!")
    time.sleep(2)
    os.system("clear")
    quit()

  else:
    colored_text("red","")
    print("I didn't get that. Try again.")
    colored_text("white","")
    print()
