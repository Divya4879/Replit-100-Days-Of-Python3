from getpass import getpass as input

print("2 Player Rock🪨 Papers📄 Scissors✂️ Game")

name1 = input("1st Player Name: ")
player1 = input("Player 1 > (enter R,P or S for rock,paper or scissors) ")

name2 = input("2nd Player Name: ")
player2 = input("Player 2 > (enter R,P or S for rock,paper or scissors) ")

if player1 == "R" or player1 == "r" or player1 == "🪨":
  if player2 == "P" or player2 == "p" or player2 == "📄":
    print(f"Congrats {name2}🥳🥳!! You won this round by your 📄.")

  elif player2 == "s" or player2 == "S" or player2 == "✂️":
    print(f"Congrats {name1}🥳🥳!! You won this round by your 🪨.")

  else:
    print("This match was a draw🫨! Try again.")



if player1 == "P" or player1 == "p" or player1 == "📄":
  if player2 == "R" or player2 == "r" or player2 == "🪨":
    print(f"Congrats {name1}🥳🥳!! You won this round by your 📄.")

  elif player2 == "s" or player2 == "S" or player2 == "✂️":
    print(f"Congrats {name2}🥳🥳!! You won this round by your ✂️.")

  else:
    print("This match was a draw🫨! Try again.")



if player1 == "S" or player1 == "s" or player1 == "✂️":
  if player2 == "R" or player2 == "r" or player2 == "🪨":
    print(f"Congrats {name2}🥳🥳!! You won this round by your 🪨.")

  elif player2 == "P" or player2 == "p" or player2 == "📄":
    print(f"Congrats {name1}🥳🥳!! You won this round by your ✂️.")

  else:
    print("This match was a draw🫨! Try again.")
