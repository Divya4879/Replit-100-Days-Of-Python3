# Day 18 Challenge - Guess the Number Game

import random  
print("Hello, Welcome to this Number Guessing Game!")
print()

num = random.randint(1, 1000000) 

print("I really don't think you can get it right😏😏! Prove me wrong if you can😁😁.")

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
