# Fake Fan Question Generator

print("A simple game to find out if you're a superfan or a fake fan of 'Harry Potter'")
print()

fan = input("Are you a fan of Harry Potter Series as well? (reply as Y or N) ")
if fan == "Y":
  
  middleName = input("What was Harry Potter's middle name? ")
  if middleName == "James":
    print("Correct!")
    subject = input("What subject did Professor Lupin teach in Hogwarts? ")
    if subject == "Defense Against the Dark Arts" or "DADA":
      print("Correct again!")

      realName = input("What was Lord Voldemort's real name? ")
      if realName == "Tom Riddle":
        print("Correct😊")
  
        owlName = input("What was the name of Harry Potter's owl? ")
        if owlName == "Hedwig":
          print("YES!!")
  
          place = input("Where did Bill Weasley work after graduation? ")
          if place == "Egypt":
            print("You did it! You are a Superfan!!")
          else:
            print("Darn! Just 1 more was left!")
        else:
          print("You got through more than half of it!")
        
      else:
        print("You got 2 correct!")
    else:
      print("This was so easy!!")
  
  else:
      print("NO!")
      print("Read the books or watch the movie again!! You are a fake fan!")

    
else:
  print("Oh well! This quiz is not for you then.")
