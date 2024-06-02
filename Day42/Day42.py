# Day 42 Challenge

import time

def type_beast(type):
  if type=="Fire":
    print("\033[31m", end=" ")
  elif type=="Water":
    print("\033[34m", end=" ")
  elif type=="Earth":
    print("\033[32m", end=" ")
  elif type=="Air":
    print("\033[0m", end=" ")

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾",end = "\n\n")

beast_details = {"Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

for key in beast_details.keys():
  beast_details[key] = input(f"Input your Beast's {key} > ").strip().title()
print()
print("****************************************")
time.sleep(1.5)
  
for key, value in beast_details.items():
  if key == "Type":
    type_beast(beast_details["Type"])
    
print()
for key,value in beast_details.items():
  print(f"{key:<15}: {value}")
