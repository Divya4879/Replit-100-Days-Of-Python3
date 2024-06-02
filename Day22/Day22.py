"""
# Day 22 Code

import random
myNumber = random.randint(1,100)
print(myNumber)

"""

"""
# Fix the code

import random

for i in range(10):
  myNumber = random.randint(1, 10)
  print(myNumber)
"""
  
# Day 22 Challenge - Guess the Number Game Upgraded

import random  
print("Hello, Welcome to this Number Guessing Game!")
print()

print("I really don't think you can get it right BTW😏😏! Prove me wrong if you can😁😁.")
print()
user = "run"
while user == "run":
  num = random.randint(1, 1000000) 
  guess = 0
  while True:
  
    user_guess = int(input("Enter a number between 1 & 1000000, and I'll tell you if it's the same guess as mine or something different: "))
    print()
  
    if user_guess < 0:
      print("Wait what!! Bye-Bye")
      exit()
  
    elif user_guess < num:
  
      print("Too Low! Try Again")
      guess += 1
  
    elif user_guess > num:
  
      print("Too high! Another Try needed")
      guess += 1
  
    elif user_guess == num:
      guess += 1
      break
  
  print(f"Congrats🥳🥳! You got it right in {guess} tries!")

  user = input("Do you wanna try again with a new number? Type 'run' to play another round." )
  if user != "run":
    print("Hope you enjoyed it! Good day")
    exit()
