# Day 48 Challenge
"""
f = open("savedFile.txt", "w")
f.write("Hello there!")
f.close()

f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"\n{whatText}")
f.close()

# I/O operation error
f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"\n{whatText}\n")

whatText = input("> ")
f.write(f"{whatText}\n")
f.close()

# Fix My Code

f = open("savedFoal.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
"""

# Day 48 Challenge
import os, time

print("🌟HIGH SCORE TABLE🌟")
print()
f = open("high.score","a+")

while True:
  
  initials, score = input("Enter the 1st 3 initials of your name and your score : ").split(" ")
  
  initials = initials.strip().upper()
  
  f.write(f"{initials} {score}\n")
  print()
  print("ADDED")
  user_prompt = input("Add another? y/n >> ")
  if user_prompt.lower()[0] == "y":
    print()
    
    time.sleep(1)
    os.system("clear")
    continue
  else:
    f.close()
    exit()
