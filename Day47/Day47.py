# Day 47 Challenge

import time,os

print("🌟Top Trumps🌟",end = "\n\n")
print("***************************************",end = "\n\n")

print("Welcome to the Top Trumps' Harry Potter Series 'Best Character' Simulator",end = "\n\n")

characters = {}
harryPotter = {
    "Intelligence": 79,
    "Handsomeness": 94,
    "Magic Power": 92,
    "Life Skills": 97
}
hermioneGranger = {
    "Intelligence": 87,
    "Handsomeness": 85,
    "Magic Power": 79,
    "Life Skills": 59
}
ronWeasley = {
    "Intelligence": 68,
    "Handsomeness": 60,
    "Magic Power": 70,
    "Life Skills": 68
}
dracoMalfoy = {
    "Intelligence": 88,
    "Handsomeness": 92,
    "Magic Power": 83,
    "Life Skills": 78
}

characters = {
  "Harry Potter" : harryPotter,
  "Hermione Granger" : hermioneGranger,
  "Ron Weasley" : ronWeasley,
  "Draco Malfoy" : dracoMalfoy
}

print("Characters: ",end = "\n\n")

for key in characters.keys():
  print(key)
print()

user_prompt = input("Do you want to add your own characters for this game? ").strip().lower()

if user_prompt[0] == "y":
  
  new_char = int(input("How many charecters do you want to create? >> "))
  print()

  for i in range(new_char):
    print(f"Character {i+1}")
    name = input("Enter name of your Harry Potter Character >> ").strip().title()
    intelligence = int(input("Enter their intelligence stats (0-100) >> "))
    handsomeness = int(input("Enter their handsomeness stats (0-100) >> "))
    magic_power = int(input("Enter their magic power stats (0-100) >> "))
    life_skills = int(input("Enter their life skills' stats (0-100) >> "))
    print()
    characters[name] = {
      "Intelligence": intelligence,
      "Handsomeness": handsomeness,
      "Magic Power": magic_power,
      "Life Skills": life_skills  
    }

  print(characters)
  print("Characters: ",end = "\n\n")

  for key in characters.keys():
    print(key)
    
print()

while True:
  print("Characters: ",end = "\n\n")

  for key in characters.keys():
    print(key)
  print()  
  print("1st Player")
  char1 = input("Choose your character >> ").strip().title()
  print()

  new_player = input("Do you have another player(y) or do you want to play with your computer(n)? >> ").strip().lower()

  if new_player[0] == "y":
    print("2nd Player")
    char2 = input("Choose your character >> ").strip().title()
    print()

  else:
      for i in range(len(characters)):
        for key in characters.keys():
          if key == char1:
            continue
          else:
            char2 = key
            break
      print()
      print(f"Computer has picked {char2}.")
  
  for key in characters.keys():
    if char1 == key:
      char1_stats = {}
      char1_stats = characters[char1]
  
    if char2 == key:
      char2_stats = {}
      char2_stats = characters[char2]
  
  while True:
    
    print("Choose a stats Criteria: ")
    print()
    
    for value in characters.values():
      for key in value.keys():
        print(key)
      break
    
    stat = input(">> ").strip().title()
    time.sleep(1)
    print(f"{char1}: {char1_stats[stat]}")
    print(f"{char2}: {char2_stats[stat]}")
    print()
    a, b = char1_stats[stat], char2_stats[stat]
    char1_wins = 0
    char2_wins = 0
    
    if a > b:
      print(f"{char1} Wins!")
      char1_wins += 1 
    
    elif b > a:
      print(f"{char2} Wins!")
      char2_wins += 1
    
    else:
      print("It's a draw!")
    print()
    time.sleep(1)
    new_round = input(f"Do you wanna compare {char1} and {char2} other stats as well?: ").strip().lower()
    
    if new_round[0] == "y":
      time.sleep(0.5)
      continue
    
    else:
      time.sleep(0.5)
      print()
      if char1_wins > char2_wins:
        print(f"********** {char1} Wins! **********")
      else:
        print(f"********** {char2} Wins! **********")
      break
  
  new_character = input("Do you want to choose other characters & play again? ").strip().lower()
  
  if new_character[0] == "y":
    print()
    time.sleep(1)
    os.system("clear")
    continue
  
  else:
    exit()
