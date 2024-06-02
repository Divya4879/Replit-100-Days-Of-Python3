"""
# Day 17 Code - continue & exit()

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()

print("The game is over! You failed")

"""

"""
# Fix the code

print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute":
    print("Game over!")
    break
  elif direction == "ladder":
    continue
else:
    print("Game over!")
    exit() 
print("Thanks for playing!")

"""

# Day 17 Challenge

from getpass import getpass as input

print("MORE EPIC 2 Player 🪨 📄 ✂️ GAME- UPGRADED")

name1 = input("1st Player Name: ")
name2 = input("2nd Player Name: ")

player1_wins = 0
player2_wins = 0

while player1_wins < 3 or player2_wins < 3:
  if player1_wins == 3:
    player = name1
    loser = name2
    print(f"Congrats {player}\U0001F973\U0001F973, you won by 3 victories over {loser}!")
    exit()
  elif player2_wins == 3:
    player = name2
    loser = name1
    print(f"Congrats {player}\U0001F973\U0001F973, you won by 3 victories over {loser}!")
    exit()
  player1 = input("Player 1 > (enter R,P or S for rock,paper or scissors) ")
  player2 = input("Player 2 > (enter R,P or S for rock,paper or scissors) ")
  
  
  if player1 == "R" or player1 == "r" or player1 == "🪨":
    if player2 == "P" or player2 == "p" or player2 == "📄":
      player2_wins += 1
      
      print(f"Congrats {name2}🥳🥳!! Your 📄 smothered {name1}'s 🪨.")
      continue   
      
    elif player2 == "s" or player2 == "S" or player2 == "✂️":
      player1_wins += 1
      
      print(f"Congrats {name1}🥳🥳!! Your 🪨 smashed {name2}'s ✂️.")
      continue   
  
    else:
      print("This match was a draw🫨! Try again.")
      continue
  
  
  
  if player1 == "P" or player1 == "p" or player1 == "📄":
    if player2 == "R" or player2 == "r" or player2 == "🪨":
      player1_wins += 1
      
      print(f"Congrats {name1}🥳🥳!! Your 📄 smothered {name2}'s 🪨.")
      continue
  
    elif player2 == "s" or player2 == "S" or player2 == "✂️":
      player2_wins += 1
      
      print(f"Congrats {name2}🥳🥳!! Your ✂️ chopped {name1}'s 📄.")
      continue
  
    else:
      print("This match was a draw🫨! Try again.")
      continue
  
  
  
  if player1 == "S" or player1 == "s" or player1 == "✂️":
    if player2 == "R" or player2 == "r" or player2 == "🪨":
      player2_wins += 1
      
      print(f"Congrats {name2}🥳🥳!! Your 🪨 smashed {name1}'s ✂️.")
      continue
  
    elif player2 == "P" or player2 == "p" or player2 == "📄":
      player1_wins += 1
      
      print(f"Congrats {name1}🥳🥳!! Your ✂️ chopped off {name2}'s 📄.")
      continue
  
    else:
      print("This match was a draw🫨! Try again.")
      continue
