# Day 54 Code

"""

import csv # Imports the csv library

with open("January.csv") as file: # Opens the csv file
  reader = csv.reader(file) # reads the contents of the csv file into the 'reader' variable
  line = 0

  for row in reader: # loop to output each row in the 'reader' variable one at a time.
    print (",  ".join(row)) # adds a comma and space and then joins data, you could try joining with tabs too with `\t`



import csv

with open("January.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  total = 0
  for row in reader: 
    print (row["Net Total"])
    total += float(row["Net Total"]) # Keeps a running total

print(f"Total: {total}") #Outputs

"""

# Fix My Code
"""
import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) 
  total = 0

  for row in reader: 
    print(row["Net Total"])
    total += float(row["Net Total"])

print(f"Total: {total}")

"""

# Day 54 Challenge

import csv,time,os

print("🌟Shop $$ Tracker🌟")
print()

print("Calculating........")
time.sleep(1)
os.system("clear")

print("🌟Shop $$ Tracker🌟")
print()

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  amount = 0
  
  for row in reader:
    amount += float(row["Cost"]) * int(row["Quantity"])
    
amount = round(amount,2)

print(f"Your shop took ${amount} today.")
