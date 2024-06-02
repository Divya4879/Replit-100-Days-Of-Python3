# Day 46 Code

"""

clue = {}
def prettyPrint():
  print()

  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()

while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")

  clue[name] = {"location": location, "weapon":weapon} 

  prettyPrint()


john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
# The first bracket contains the key that references the sub dictionary. The second bracket contains the key that references the sub item. This will output '75'.


# Fix the Code

john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
print(courseProgress["Janet"]["streak"])

"""

# Day 46 Challenge
import os, time

def element_beast(element):
  if element=="Fire":
    print("\033[31m", end=" ")
  elif element=="Water":
    print("\033[34m", end=" ")
  elif element=="Earth":
    print("\033[32m", end=" ")
  elif element=="Air":
    print("\033[0m", end=" ")
  else:
    print("\033[1;33m", end=" ")

title = "🌟MokeBeast Generator🌟"
print(f"{title:^60}")
print()
mokeBeast = {}

def prettyPrint():
  print()
  for key, value in mokeBeast.items():
    name = "NAME"
    print(f"{name:^10}",end = "|")
    for subkey,subvalue in value.items(): 
      if subkey == "MP":
        print(f"{subkey:^10}")
      else:
        print(f"{subkey:^10}",end = " | ")
    break
  
  for key, value in mokeBeast.items():
    print(f"{key:^10}",end = "|")
    for subkey,subvalue in value.items(): 
      if subkey == "Element":
        element_beast(mokeBeast[key]["Element"])
      if subkey == "MP":
        print(f"{subvalue:^10}")
      else:
        print(f"{subvalue:^10}",end = " | ")
    element_beast("Air")
    
 
while True:
  NAME = input("Input the beast name > ")
  print()
  
  element = input("Input the beast element > ").strip().capitalize()
  print()
  
  move = input("Input the beast special move > ").strip().title()
  print()
  
  HP = int(input("Input the beast starting HP > "))
  print()       

  MP = int(input("Input the beast starting MP > "))
  print()
  
  mokeBeast[NAME] = {"Element": element, "Special Move" : move, "HP" : HP, "MP": MP}
  
  print("----------------------------------------------------------",end = "\n\n")
  prettyPrint()
  user_prompt = input("Another character? y/n >> ").strip().lower()
  if user_prompt[0] == "y":
    time.sleep(1)
    os.system("clear")
    
  else:
    os.system("clear") 
    prettyPrint()
    exit()
