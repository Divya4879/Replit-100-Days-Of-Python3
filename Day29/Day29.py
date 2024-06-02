"""
# Print statement parameters- end, sep, removing cursor

for i in range(0, 100):
  print(i, end="\v")

print("If you put")
print("\033[33m", end="") #yellow
print("nothing as the")
print("\033[35m", end="") #purple
print("end character")
print("\033[32m", end="") #green
print("then you don't")
print("\033[0m", end="") #default
print("get odd gaps")

print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")

print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

# The cursor will be removed

import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")

# To print the cursor back on-

print("\033[?25h", end="")

"""

#Day 29 Challenge
import time

def colors_spaces(color,word):
  if color=="red":
    print("\033[31m", word, sep="", end=" ")
  elif color=="blue":
    print("\033[34m", word, sep="", end=" ")
  elif color=="green":
    print("\033[32m", word, sep="", end=" ")
  elif color=="purple":
    print("\033[35m", word, sep="", end=" ")
  elif color=="cyan":
    print("\033[36m", word, sep="", end=" ")
  elif color=="dark_gray":
    print("\033[1;30m", word, sep="", end=" ")
  elif color=="yellow":
    print("\033[1;33m", word, sep="", end=" ")
  elif color=="light_green":
    print("\033[1;32m", word, sep="", end=" ")
  elif color=="light_purple":
    print("\033[1;35m", word, sep="", end=" ")
  else:
    print("\033[0m", word, sep="", end=" ")
  

print("My Colorful Program", end= "\n\n")
time.sleep(1)
print("With my ",end = "")
colors_spaces("green","new program")
colors_spaces("blue",'I can just call red ("and")')
colors_spaces("red", "and")
colors_spaces("purple","that word will appear in the color I set it to.")
time.sleep(0.5)
print(end = "\n\n")

colors_spaces("no","With no")
colors_spaces( "cyan","weird gaps",)
colors_spaces("light green","in between")
time.sleep(0.5)
print(end = "\n\n")

colors_spaces("light_purple", "Pretty exciting")
time.sleep(0.5)
print(end = "\n\n")
colors_spaces("end","")
