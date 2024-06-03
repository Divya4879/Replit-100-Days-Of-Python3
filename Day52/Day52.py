# Day 52 Code - Try & Except
"""

debugMode = True
myStuff = []

# We can tell except what type of error(s) to look for. Exception (capital 'E') means 'every type'. I've captured the error type in the 'err' variable and printed it out to tell me what the error is.


try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
  
# Try to find a file called 'Stuff.mine' and open it

# except Exception as err:
#   print("ERROR: Unable to load")

# # If the file can't be found, show the error instead of crashing the whole program
#   print(err)

except Exception:
  print("ERROR: Unable to load")
  if debugMode:
    print(traceback)

for row in myStuff:
  print(row)

"""

"""
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
  
except Exception as err:
  print(err)
  print("Try again!")
  
for row in myStuff:
  print(row)

"""

# Fix My Code

"""
myStuff = []

try:  
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

except Exception as err:
  print(err)
  
for row in myStuff:
  print(row)

"""

# Day 52 Challenge
import os, time

pizzaOrder = []

try:
  f = open("pizza.order","r")
  pizzaOrder = eval(f.read())
  f.close()

except Exception as err:
  print(err)

def add_pizza():
 
  name = input("Name: ").strip().title()
  toppings = input("Toppings: ").strip().capitalize()
  size = input("Size (s/m/l): ").strip().upper()[0]
  
  integer = True
  while integer:
    try:
      quantity = int(input("Quantity: "))
  
    except Exception:
      print("Please try again and enter a numeric value")
      continue

    integer = False
  
  total =  quantity * 75
  
  if size == "S":
    total *= 1
  elif size == "M":
    total *= 1.25
  elif size == "L":
    total *= 1.5
    
  row = [name, toppings, size, quantity,total]
  pizzaOrder.append(row)

def view_choice():
  
  name = "Name"
  top = "Topping"
  size = "Size"
  quantity = "Quantity"
  total = "Total"
  print(f"{name:^20}  {top:^12}  {size:^7}  {quantity:^8} {total:>7}")
  print()
  
  for row in pizzaOrder:
    print(f"{row[0]:^20}  {row[1]:^12}  {row[2]:^7}  {row[3]:^8}  {row[4]:^7}", end="")
    print()
  time.sleep(3)

while True:
  os.system("clear")
  print("🌟Divya's Healthy Pizzas🌟")
  print()
  
  user_prompt = input("1: Add Pizza\n2: View your Pizzas\n>> ").strip()
  time.sleep(0.5)
  os.system("clear")
  if user_prompt == "1":
    add_pizza()
  
  elif user_prompt == "2":
    view_choice()

  f = open("pizza.order","w")
  f.write(str(pizzaOrder))
  f.close()
