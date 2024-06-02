"""

# Day 30 Code

name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print(response)

# New code

for i in range(1, 31):
  print(f"Day {i: ^2} of 30")

food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

# Fix the code

response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, location=location, color=color,friend= friend)

print(response)

"""

print("30 Days Far🥳!",end="\n\n")

day = 1
while day <= 30:
  print(f"Day {day}")
  user_response = input("")
  response1 = f"\033[1mYou thought Day {day} was\033[0m"
  response2 = f"\033[1m{user_response}\033[0m"
  print(f"{response1:^50}")
  print(f"{response2:^50}")
  day += 1
