print("Grade Generator")
print()

subject = input("Name of Exam: ")
max_score = int(input("Enter the maximum possible score: "))

your_score = float(input("Enter your score here: "))

percent_score = (your_score / max_score) * 100
percent = round(percent_score, 2)

if percent < 50:
  grade = "U"
  print(f"You got {percent}% and a {grade} grade👿. You didn't even scrape through your exam!")

elif percent >= 50 and percent <= 59:
  grade = "D"
  print(f"You got {percent}% and a {grade} grade😡. You need to study harder and do better!")

elif percent > 59 and percent < 69:
  grade = "C"
  print(f"You got {percent}% and a {grade} grade😠. You gotta do better than this!")

elif 69 < percent < 80:
  grade = "B"
  print(f"You got {percent}% and a {grade} grade😤. You know you can do better than this, I believe in you!")

elif 79 < percent < 90:
  grade = "A"
  print(f"Great😊! You got {percent}% and an {grade} grade.")

elif 89 < percent < 101:
  grade = "A+"
  print(f"Amazing 🤩! You got {percent}% and an {grade} grade.")

else:
  print("Enter correct values")
  
