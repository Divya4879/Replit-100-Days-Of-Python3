# Day 60 Code

"""
import datetime

date = datetime.date(year = 2024, month = 5, day = 3)
print(date)

today = datetime.date.today()

# This code outputs the current date from your computer's clock.

print(type(today)) #<class 'datetime.date'>
print(today)

"""

# import datetime

# day = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))

# date = datetime.date(year,month,day)
# print(date)

# Get all input as numbers. We're not at text input for months yet.

"""

import datetime

today = datetime.date.today()
difference = datetime.timedelta(days=14)
# The difference I want

print(today + difference)
# Add today to the delta difference to see the date in 14 days time.

"""

"""
import datetime

today = datetime.date.today() # Today's date

holiday = datetime.date(year = 2022, month = 10, day = 30) # The date of my holiday

if holiday > today: # If my holiday is in the future
  print("Coming soon")
elif holiday < today: #If my holiday date has passed
  print("Hope you enjoyed it")
else: # If my holiday date is today
  print("HOLIDAY TIME!")
  
"""

# Fix the Code

# import datetime

# today = datetime.date.today() 

# holiday = datetime.date(year = 2024, month = 6, day = 20) 

# if holiday > today: 
#   print("Coming soon")
# elif holiday < today: 
#   print("Hope you enjoyed it")
# else:
#   print("HOLIDAY TIME!")

# Day 60 Challenge

import datetime

print("🌟Event Countdown Timer🌟")
print()

today = datetime.date.today()

event = input("Input the event > ").strip().title()
print()

year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))

event_date = datetime.date(year,month,day)

difference = abs((event_date - today)).days

print()

if today > event_date:
  print(f"🥺(ᴗ_ ᴗ。)🥀❤️‍🩹 {event} was already over. I really hope you enjoyed it! 🤞🤗🍀🥹💫")

elif today < event_date:
  print(f"🪩🫧🍸🥂🫧✧˖° {event} is coming up soon 🪩🫧🍸🥂🫧✧˖°")

else:
  print(f"😎👌🔥💃🏻🕺🏽 {event} is today! Enjoy your day!! 😎👌🔥💃🏻🕺🏽")
