"""
# Day 15 Code

count = 1
while count <= 100:
  print(count)
  count += 1

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")

"""

"""
# Fix the Code

counter = 0
while counter < 25:
  print(counter)
  counter += 1

counter = 0
while counter <= 12:
  print(counter)
  counter += 1

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")

"""

# Day 15 Challenge - A Children's Game of Animal Sounds

print("This is a simple game, in which you can type an animal's, a bird's or a few insects' name, and get to hear(actually, just see) the sound they produce.")
print()

print("Disclaimer: This list is not intensive, it's based on a very small dataset.")

print()
print()

name = input("Enter your name: ")
 
print()
exit_game = ""


while exit_game != "Y":
  animal = (input("Which animal do you want to hear from? ")).capitalize()
  print()
  if animal == "Cow":
    pic = "🐄"
    animalSound = "moo"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Tiger":
    pic = "🐅"
    animalSound = "growl"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Dog":
    pic = "🐕"
    animalSound = "Woof"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Cat":
    pic = "🐈"
    animalSound = "Meow"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Pig":
    pic = "🐖"
    animalSound = "oink"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Elephant":
    pic = "🐘"
    animalSound = "bahruuuuuuhhhhaaaaa"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Horse":
    pic = "🐎"
    animalSound = "neigh"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Mouse":
    pic = "🐁"
    animalSound = "squeak"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Duck":
    pic = "🦆"
    animalSound = "quack"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Snake":
    pic = "🐍"
    animalSound = "hisss...."
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Frog":
    pic = "🐸"
    animalSound = "croak"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Bat":
    pic = "🦇"
    animalSound = "screech"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Rooster":
    pic = "🐓"
    animalSound = "Cock-a-doodle-doo"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Parrot":
    pic = "🦜"
    animalSound = "sqwak"
    print(f"Hi {name}")
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound} and says hi!!
    Wanna hear more sounds?  
      """)

  elif animal == "Owl":
    pic = "🦉"
    animalSound = "hoot"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Fly":
    pic = "🪰"
    animalSound = "buzz..."
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)

  elif animal == "Zebra":
    pic = "🦓"
    animalSound = "bray"
    print(f"""Hello {name}😁!
      Our friendly {animal}{pic} greets you with a {animalSound}!
    Wanna hear more sounds?  
      """)
    
  else:
    print("Sorry, the animal/bird/insect you entered isn't in the dataset!")
    
  exit_game = input("Do you want to exit this game? (Enter Y if you want to leave 🥹) ")

print("Hope you had some fun 😊")
