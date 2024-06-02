# Day 9 Challenge

print("Generation Generator")
print()

birthYear = int(input("Which year were you born in? "))

if birthYear <= 1946:
  print("Have a great day sir/madam 🫡! You are of a Traditionalists generation. Cultures grow on the vine of tradition.")

elif birthYear >= 1947 and birthYear <= 1964:
  print("""Hello Baby Boomer 🙂!
Do you value to be given individual choices and do you live with an optimistic attitude?
Also, I love your motto:- 
       "Everything is possible."
  """)

elif birthYear >= 1965 and birthYear <= 1981:
  print("""Hello, Generation X 😊!
I love your motto of "Life's too short to waste on regret".
Also, this generation has the best reviews on the net so far:-
This generation is known for their resilience and determination.   
  """)

elif birthYear >= 1982 and birthYear <= 1995:
  print("Hello Millenials!")
  print("Money can't buy us happiness, that's damn true! But it can get us whatever we want, to take care of our loved ones, to have freedom to work for our passion, and not just out of a necessity.")

elif birthYear >= 1996:
  print("Hello, Generation Z!!😁")
  print("“Who I am today may not be who I am tomorrow. Change, grow and adapt with me as my identity will always be evolving.“")
  print("I get it, I really do! But if you change, change only  for the better!")

else:
  print("Enter your birth year again!")
