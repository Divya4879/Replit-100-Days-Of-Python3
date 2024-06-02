# Day 45 Challenge

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
priorityList = []

def add_task():
  task = input("Which task do you want to add in your list? ").strip().title()
  for row in toDoList:
    for item in row:
      if item == task:
        colored_text("blue","")
        print(f"{task} is already in your agenda for today.")
        time.sleep(1)
        return
  deadline = input("When is it due? ").strip().title()
  priority = input("What's its priority level? ").strip().capitalize()
  row = [task,deadline,priority]
  toDoList.append(row)
  time.sleep(0.5)
  print()
  colored_text("purple","")
  print(f"{task} is added in your To-Do list")
  time.sleep(1)
  view_list(toDoList)
  time.sleep(1)
  

def edit_task():
  task = input("Which task from your agenda do you want to edit? ").strip().title()
  for row in toDoList:
    if task in row:
        print()
        toDoList.remove(row)  
        task = input("New Task: ").strip().title()
        deadline = input("New Deadline: ").strip().title()
        priority = input("New Priority: ").strip().capitalize()
        row = [task,deadline,priority]
        toDoList.append(row)
        colored_text("purple","")
        print("Edited!")
        view_list(toDoList)
        time.sleep(1)
        break


def remove_task():
  task = input("Which task do you want to remove from your list? ").strip().title()
  for row in toDoList:
    for item in row:
      if item == task:
        user_query = input(f"Do you really want to remove {task} from your list? ")
        if user_query.strip().lower()[0] == "y":   
          toDoList.remove(row)
          colored_text("purple","")
          print(f"Congratulations🥳,{task} has been completed & removed from your to-do list!")
          time.sleep(1)
          view_list(toDoList)
          break
        else:
          continue

    else:
      colored_text("red","")
      print(f"{task} wasn't in your To-Do List!")
      print("Try again!\n")
      time.sleep(1)
      colored_text("white","")
      return


def view_list(list):
  os.system("clear")
  colored_text("green","")
  title = "T0-DO LIST"
  print(f"{title : ^44}",end="\n\n")
  for i in range(len(list)):
    for item in list[i]:
      if list[i][len(list[i])-1] == item:
        print(f"{item : ^15}", end="")
      else:
        print(f"{item : ^15}", end="|")
    print()
  colored_text("white","")
  print()


def view_priority():
  chosen_priority = input("Which priority tasks?: ").strip().capitalize()
  for row in toDoList:
    for item in row:
      if item == chosen_priority:
        print(row)
        priorityList.append(row)
        continue
  time.sleep(4)
  print(priorityList)
  view_list(priorityList)


while True:
  os.system("clear")
  colored_text("yellow","")
  print("          🌟Life Organizer🌟")

  user_prompt = input("\n1. Add a task\n2. Edit a task\n3. Remove an item from your list\n4. View your list\n5. Create a new list\n6. Quit this application\n\n>> ")
  colored_text("white","")
  time.sleep(0.5)
  print()

  if user_prompt == "1":
    add_task()

  elif user_prompt == "2":
    edit_task()
    time.sleep(1) 

  elif user_prompt == "3":
    remove_task()

  elif user_prompt == "4":
    print()
    view_choice = int(input("1. View All\n2. View by Priority\n\n>>"))
    if view_choice == 1:
      view_list(toDoList)
    elif view_choice == 2:
      view_priority()
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
