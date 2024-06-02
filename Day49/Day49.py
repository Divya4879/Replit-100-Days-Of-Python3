# Day 49 Challenge

"""
# f.read()
f = open("high.score", "r")
contents = f.read()
f.close()

contents = contents.split() #added split here
print(contents)

# f.readline()
f = open("high.score","r")

while True:
  
  contents = f.readline().strip()
  
  if contents == "":
    break
    #The last line in the file will be a blank
    #We break the loop if the line read is a blank
  
  print(contents)
  # Moved the print after the break so it won't output the final blank line.

f.close()


f = open("high.score","r")
while True:
  contents = f.readline().strip()
  

  if contents == "":
    break
  print(contents)

f.close()
"""

# Fix My Code
"""
f = open("high.score","r")
while True:
  contents = f.readline().strip()
  if contents == "":
    break
  print(contents)

f.close()

"""

# Day 49 Challenge
import time

print("🌟Current Leader🌟")
print()

print("Analyzing high scores......",end = "\n\n")
time.sleep(1)

f = open("high.score","r")
highest_score = 0
highest_scorer = ""

while True:
  
  scores = f.readline().strip()
  
  if scores == "":
    break
    
  score = int(scores.split(" ")[1])
  scorer = scores.split(" ")[0]
  
  if score > highest_score:
    highest_score = score
    highest_scorer = scorer

f.close()

print(f"Current leader is {highest_scorer} with the highest score of {highest_score}.")
