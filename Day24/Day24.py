"""
# Day 24 Code

def whichCake(ingredient,base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")

  print(f"So, you want a {ingredient} cake on a {base} with {coating} on top?")

whichCake("chocolate", "bread", "icing")
whichCake("broccoli", "coconut flour", "spinach")
whichCake("strawberry", "ice cream", "chocolate")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)

"""

"""
# Fix the code

def pizza_order(topping1,topping2):
  if topping1 == "pineapple":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
    print(topping2, "sounds delicious, much better than" , topping1)

topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)

"""

print("Infinity Customized Dice 🎲")
rounds = "yes"
sides =  int(input("Enter the no of sides you wanna have on your special dice: "))

def roll_dice(sides):
  import random
  roll_result = random.randint(1,sides)
  print(f"You rolled {roll_result}.")

roll_dice(sides)

while rounds != "no":
  if rounds != "yes":
    print("I didn't get that! Try again.")
  rounds = input("Wanna roll it again? ")
  roll_dice(sides)


if rounds == "no":
  exit()
