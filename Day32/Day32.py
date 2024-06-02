"""
# Day 32 Code- Lists

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[1])
for i in timetable:
  print(i)

print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
timetable[4]= "Watch TV"
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])

timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)


# Fix the code

grocery_list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print(f"The first grocery item to buy is {grocery_list[0]}.")

"""

# Day 32 Challenge
import random

print("Welcome to my multilingual greeting application",end="\n\n")

name = input("May I have your name, please? ")
greetings = ["Namaste", "Bonjour","Hola","Nǐn hǎo","Ciao","Hallo","Olá","Anyoung haseyo","Asalaam alaikum","Hoi","Selamat siang","Hey"]

user_greeting = greetings[random.randint(0,len(greetings)-1)]

print()

print(f"{user_greeting} {name}! Hope you are having a nice day 😊")
