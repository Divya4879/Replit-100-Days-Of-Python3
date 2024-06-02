# Day 41

"""
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])

# 👉 The .items() function returns the key name and value. Note that I've supplied the loop with two arguments: 'name' and 'value').

myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if name == "strength":
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")


myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for key,value in myDictionary.items():
  print(f"{key}:{value}")


# Fix The Code
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")

"""

# Day 41 Challenge
print("🌟Website Rating🌟",end="\n\n")

user_website = {"name": None, "url": None, "desc": None, "rating": None}

# user_prompt = input("Enter your website's name, it's URL, a description, and its rating out of 5 (answer different ques with , in between): ")


# user_website["name"], user_website["url"], user_website["desc"], user_website["rating"] = user_prompt.split(",") 

for name in user_website.keys():
  user_website[name] = input(f"Input the {name}: ").strip()

print()
print("*****",end="\n\n")

for key, value in user_website.items():
  print(f"{key}:   {value}")
print()
print("*****")
