import os
import time,datetime

colors = {
  "red": "\033[31m",
  "blue": "\033[34m",
  "green": "\033[32m", 
  "purple": "\033[35m", 
  "cyan": "\033[36m", 
  "dark_gray": "\033[1;30m",
  "yellow" : "\033[1;33m",
  "light_green" : "\033[1;32m",
  "light_purple" : "\033[1;35m",
  "default" : "\033[0m"
 }

def color(arg):
  for key in colors:
    if arg == key:
      return colors[key]

def pretty_print_colors(list):
  print()
  for item in list:
    print(f"{color(item)}{item:^50}")
   
  time.sleep(2.5)
  os.system("clear")


def pretty_print_list(list):
  time.sleep(2)
  os.system("clear")
  print(f"{list[0]:^40}")
  print()
  for i in list:
    if i != list[0]:
      print(f"{i:^40}")


def add_list(list):
  more_data = True
  while more_data:
    data = input("Item: ")
    list.append(data)
    prompt = input("Another item?(y/n) ").strip().lower()[0]
    if prompt == "n":
      more_data = False
  

def remove_item(list):
  item = input("Which item do you wanna remove? ")
  if item in list:
    list.remove(item)    
    
def create_list():
  name = input("Name of List: ").strip().upper()
  li= []
  li.append(name)
  add_list(li)
  
  view = input("Wanna view your items? ")
  time.sleep(1)
  os.system("clear")
  
  if view.strip().lower()[0] == "y":
    pretty_print_list(li)
    
  print()
  removeItem = input(f"Do you want to remove an item from {name}? ").strip().lower()[0]
  
  if removeItem == "y":
    remove_item(li)
  pretty_print_list(li)
  time.sleep(1.5)
  os.system("clear")

def pretty_print_dict(di,name):
  time.sleep(2)
  os.system("clear")
  print(f"{name:^40}")
  print()
  for key,value in di.items():
    print(f"{key:>18}: {value:<12}")
  print()

def remove_item_dict(dict_user):
  item = input("Item to be removed: ")
  
  for key in dict_user:
    if dict_user[key] == item:
      del dict_user[key]
      return

def create_dict(): 
  dict_user= {}
  name = input("Name of your dict: ")
  new_items = True
  while new_items:
    key = input("Key: ")
    value = input("Value: ") 
    dict_user[key] = value
    
    prompt = input("Add more items? ").strip().lower()[0]
    if prompt == "n":
      new_items = False
  print()
  view = input("Wanna view your items? ")  
  
  if view.strip().lower()[0] == "y":
    pretty_print_dict(dict_user,name)

    removeItem = input(f"Do you want to remove an item from {name}? ").strip().lower()[0]
    if removeItem == "y":
      remove_item_dict(dict_user)
      
      pretty_print_dict(dict_user,name)
      time.sleep(2)
      os.system("clear")

def remove_2d_entry(list):
  day = int(input("Enter day of the workout: "))
  month = int(input("Enter month of the workout: "))
  year = int(input("Enter year of the workout: "))
  date_delete = str(datetime.date(year,month,day))
  count = 0
  for i in list:
    if i[3] == date_delete:
      del list[count]
      return
    count += 1


def add_2dList():
  twoD_List = []
  new_entry = True

  while new_entry:
    workout = input("Workout Type: ")

    duration = int(input("For how long did it last?: "))

    intensity = int(input("Rate the intensity on a scale of 0-10: "))

    days_ago = int(input("How many days ago did you do this? "))

    today = datetime.date.today()

    date = str(today - datetime.timedelta(days = days_ago))
    
    row = [workout,duration,intensity,date]
    twoD_List.append(row)

    user_prompt = input("Wanna add another entry?: ").strip().lower()[0]
    if user_prompt == "n":
      new_entry = False

  view_2d(twoD_List)
  os.system("clear")
  user_prompt = input("Wanna delete an entry?: ").strip().lower()[0]
  if user_prompt == "y":
    remove_2d_entry(twoD_List)

  view_2d(twoD_List)

def view_2d(twodList):
  time.sleep(1)
  os.system("clear")
  workout = "Workout"
  duration = "Duration(mins)"
  intensity = "Intensity"
  date = "Date"

  print(f"{workout:^10} {duration:^12}  {intensity:^11} {date:^12}")
  print()

  for row in twodList:
    print(f"{row[0]:^10}  {row[1]:^10}  {row[2]:^9}  {row[3]:>16}", end="")
    print()
  time.sleep(3)
