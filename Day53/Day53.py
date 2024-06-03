# Day 53 Challenge

import time,os

inventory = []

try:
  f = open("inventory.txt","r")
  inventory = eval(f.read())
  f.close()

except Exception as err:
  print(err)

# except:
# pass

def add_item():
  new_item = input("Input the item to add: > ").strip().title()
  inventory.append(new_item)
  print()
  print(f"{new_item} is added to your inventory.")

def remove_item():
  item = input("Input the item to remove: > ").strip().title()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} has been removed from your inventory.")
    return

  print(f"{item} wasn't in your inventory!")

def remove_all():
  itemToBeRemoved = input("Input the item to remove: > ").strip().title()

  if itemToBeRemoved in inventory:
    for i in range(inventory.count(itemToBeRemoved)):
      for item in inventory: 
        if item == itemToBeRemoved:
          inventory.remove(item)
    print(f"All instances of {item} has been removed from your inventory.")
  

  else:
    print(f"{itemToBeRemoved} wasn't in your inventory!")

def view_inventory():
  os.system("clear")
  print("          🌟Divya Limited Inventory🌟")
  print("          ============================")
  print()
  
  i = set(inventory)
  for item in i:
      print(f"{item:>30}    {inventory.count(item)}")
  time.sleep(1.5)

def view_one():
  item = input("Input the item to view: >> ").strip().title()
  if item in inventory:
    print(f"You have {inventory.count(item)} {item}s in your inventory.")
    time.sleep(1.5)
    return
    
  print(f"{item} wasn't in your inventory!")

while True:
  os.system("clear")
  print("          🌟Divya Limited Inventory🌟")
  print("          ============================")
  print()
  
  user_input = input("1: Add\n2: Remove\n3: View\n4: Exit\n\n>> ")
  
  os.system("clear")
  if user_input == "1":
    add_item()
  
  elif user_input == "2":
    prompt = input("1: Remove all instances of an item\n2: Remove 1 instance of an item\n\n>>")
    if prompt == "1":
      remove_all()
    elif prompt == "2":
      remove_item()
  
  elif user_input == "3":
    prompt = input("1: View All\n2: View a specific item\n\n>> ")
    if prompt == "1":
      view_inventory()

    elif prompt == "2":
      view_one()

  elif user_input == "4":
    exit()

  time.sleep(1)
  
  f = open("inventory.txt","w")
  f.write(str(inventory))
  f.close()
