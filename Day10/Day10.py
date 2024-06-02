# Day 10 Challenge - Split Bill Calculator

print("A simple calculator to split the bill between people")
print()

bill = float(input("What's the bill amount? "))
tipPercent = int(input("Decide how much amount do you want to pay as tip? (15, 18 and 20 for 15%,18% & 20% respectively.) "))

totalBill = bill * ((100 + tipPercent)/100)

noOfPeople = int(input("How many people are at your table? "))

individualPay = round(float(totalBill/noOfPeople), 2)

print(f"Alright folks! Every one of you gotta pay ${individualPay} each!")
