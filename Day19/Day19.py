"""
# Day 19 Code - for loop & range()

for counter in range(10):
  print(counter)

"""

"""
# Fix the Code

total = 10
for counter in range(100):
  total += counter
  print(total)

"""

# Day 19 Challenge

print("Loan Calculator")
print()

print("Calculating how much money you owe for a loan of $1000 with a 5% APR")
print()

loan = 1000
rate_of_interest = 0.05
amount_owed = loan

for yrs in range(10):
  amount_owed *= 1.05
  amount_owed = round(amount_owed,2)
  yr = yrs + 1
  print(f"Year {yr}: Amount you owe is ${amount_owed}")
