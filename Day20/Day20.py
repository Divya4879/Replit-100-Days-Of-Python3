"""
# Day 20 code

for i in range(100, 110):
  print(i)

for i in range (0, 1000000, 25):
  print(i)

"""

"""
# Fix the Code

for i in range (20, 40):
  print(i)

"""

# Day 20 Challenge
print("WELCOME TO MY LIST GENERATOR")
print()
print("This is a customizable list generator of Whole numbers.")
print()

start = int(input("Enter the 1st number of the list: "))
end = int(input("Enter the second last number of the list: "))
increment = int(input("Enter the increment/decrement that you wanna have between the nos: "))

print("List :-")
for list_item in range(start, end, increment):
  print(list_item)
