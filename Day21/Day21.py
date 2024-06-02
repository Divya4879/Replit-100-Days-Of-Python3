# Day 21 Challenge

print("Multiple Table Quiz")
print()
print("Let's test your multiplication skills by a number of your choice")
print()

user_name = input("Enter your name: ")
no = int(input("Enter a number of your choice, about which you're sure about  your multiplication skills: "))


correct = 0
for i in range(1,11):
  ans = i * no
  user_ans = int(input(f"{i} * {no} = "))
  if user_ans == ans:
    print("Correct🥸")
    correct += 1
  else:
    print(f"Nope, you got it wrong! The right answer is {ans}.")

if correct == 10:
  print(f"Congrats {user_name}🤩🤩! You got 10 out 10, a perfect score.")

elif 6<correct<10:
  print(f"Congrats {user_name}🥳🥳! You got {correct} out 10.")

elif 3<correct<7:
  print(f"Hey {user_name}! You got {correct} out 10.🙂")

elif 1<correct<3:
  print(f"Aloha {user_name}! You got {correct} out 10.🙄")

else:
  print(f"Wait what, you got 0 out of 10, from a no. of your choice💀💀?? Goodbye, forever {user_name}!")
