# Day 37 Code
"""

myString = "Hello there my friend."
print(myString[0])
print(myString[6:11])

# This code outputs the 'H' from 'Hello'
myString = "Hello there my friend."
print(myString[:11])

# This code outputs 'Hello there'.
myString = "Hello there my friend."
print(myString[::-1])
# This code outputs 'my friend.'.
myString = "Hello there my friend."
print(myString[0:5:2])

# This code outputs 'Hlo' (every second character from 'Hello').
myString = "Hello there my friend."
print(myString[::3])
print(myString.split())
# This code outputs 'Hltrmfe!' (every third character from the whole string).

myString = "Hello there my friend."
print(myString[0:5])

# The second argument should always be one more than the index of the final character.

# Fix The Code

myString = "Hello there my friend."
print(myString[:4:1])

# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[:11])

"""

# Day 37 Challenge
import time

print("🌟Star Wars Name Generator🌟")
print()
user_name = input("Enter your first name, last name, mum's maiden name, and the city you're born in: ").strip().lower().split()

user_first_name, user_last_name, maiden_name, city = user_name

star_wars_name = f"{user_first_name[:3]}{user_last_name[:3]} {maiden_name[:2]}{city[:-4:-1]}".title()

print()
time.sleep(1)

print(f"Your Star Wars name is {star_wars_name}")
