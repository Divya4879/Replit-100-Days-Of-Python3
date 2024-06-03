# Day 57 Code

# def reverse(value):
#   if value <= 0:
#     print("Done!")
#     return
#   # This `if` provides the 'stop' condition for the program. Otherwise it would run forever.

#   else: # if we're not at the stop condition.
#     for i in range(value):
#       print("💯", end="") # Outputs 'value' emojis
#     print() # New line
#     reverse(value - 1) # takes 2 off the value and calls the subroutine again with this new number. Eg if value was 7 it would call 'reverse(value)' again with value as 5.
# reverse(10)

"""
def reverse(value):
  if value <= 0:
    return
  for i in range(value):
    print("💯", end="") 

  print() 
  reverse(value - 1)
reverse(10)

"""

# Day 57 Challenge

import os,time

def factorial(n):
  if n <= 1:
    return 1

  elif n >= 1:
    return (n * factorial(n-1))

while True:
  integer = True
  
  print("🌟Factorial Finder🌟")
  print()
  while integer:
    try:
      no = int(input("Input a number > "))
      integer = False
      
    except:
      print("Please input an integral value.")
      print()
      continue
    
  
  fact = factorial(no)
  print(f"\nThe factorial of {no} is {fact}.")
  time.sleep(2)
  os.system("clear")
