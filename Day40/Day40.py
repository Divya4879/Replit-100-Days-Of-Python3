# Day 40 Code
"""

myUser = {"name": "Divya", "age": 128}

myUser["name"] = "The legendary Divya"
print(myUser)

# This code outputs 'name:'the legendary Divya', 'age':'128.

myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

myUser = {"name": "David", "age": 128}
# The key, name, in the dictionary should be inside quotes.
print(myUser["name"])

myUser = {"name":"David", "age": 128}
myUser["age"] = 129
# A dictionary can't have two keys with the same name. It always overrides the previous one.
print(myUser)


# Fix the Code

myUser = {"name":"Andy", "age":128}
myUser["age"] = 129

print(myUser["name"])

"""

# Day 40 Challenge
import time

print("🌟Contact Card🌟")
print()
user_details = {}

user_details["name"] = input("Input your name > ").strip().capitalize()
print()

user_details["D.O.B."] = input("Input your date of birth > ").strip()
print()

user_details["telephone-no"] = input("Input your telephone number > ").strip()
print()

user_details["email"] = input("Input your email > ").strip()
print()

user_details["address"] = input("Input your address > ").strip().title()
time.sleep(1.5)
print()

print(f"Hi {user_details['name']} 🤗. Our dictionary says that you were born on the auspicious day, on {user_details['D.O.B.']}, we can contact you on {user_details['telephone-no']}, email you at {user_details['email']}, or write to {user_details['address']}.")
