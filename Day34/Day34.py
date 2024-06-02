# Day 34 Code
"""
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for email in listOfEmail: 
    print(email)
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()  
  time.sleep(1)
  os.system("clear")


import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")






import os, time
listOfFood = []

def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 1 
  for order in listOfFood: 
    print(f"{counter}: {order}") 
    counter += 1 
  time.sleep(1)
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
    prettyPrint() 
  time.sleep(1)
  os.system("clear")

"""
# Day 34 Challenge

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index}: {listOfEmail[index]}") 
    index += 1 
  time.sleep(1)

def spamming():
  os.system("clear")
  for index in range(10):
    email_address = listOfEmail[index]
    print(f"""Dear {email_address}
Hello there! Hope you have had a nice day so far, and if it wasn't, do something about it. BTW, although it's intended to be a spam email, I just wanted to clarify that I really didn't want to do it.It's all coz of the 100 Days of Python challenge by Replit Day 33 assignment that I'm doing this.

Sincerely sorry,
Divya
    """)
    time.sleep(2)
    os.system("clear")
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email Address> ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email Address> ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 

  elif menu == "4":
    spamming()
  time.sleep(1)
  os.system("clear")
