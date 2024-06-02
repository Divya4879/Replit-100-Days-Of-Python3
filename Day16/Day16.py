"""

# Day 16 Code

while True:
  print("It's time for Day 16 today")
  prompt = input("Do you wanna keep going at it? (type no if you wanna stop) ")
  if prompt == "no":
    break

print("Aww! We have little time left, don't we 🥺")

"""

"""
# Fix the code

while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")

"""

# Day 16 Challenge - My Fav Song Lyrics

print("Welcome to a pretty simple game")
print("Fill in the blanks to complete this great song, my favourite 😍")
print("Let's see if we have something in common!")

name = input("Enter your name: ")

counter = 1

while True:
  
  print("""Please, see me
  _______ out for someone I can't see""")
  user_ans = input("Enter the missing word: ")
  if user_ans != "Reaching":
    if counter > 9:
      print("You know what, GOOD BYE😠😠!!")
      break
    print("Nope, try again")
    counter += 1
    
    
  else:
      if counter == 1:
        emoji = "🥰"
      elif 1 < counter < 5:
        emoji = "😄"
      elif 4 < counter < 9:
        emoji = "🙂"
      
      print(f"Hey, {name}{emoji}! You got the right word at your {counter} round.")
      break
