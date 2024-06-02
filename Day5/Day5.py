# "Which Character are You" Generator

print("Harry Potter Character Generator")

print("Answer these questions as Y or N, and let's find which Harry Potter character suits you the best")

print("Disclaimer: It will only consider their character/behaviour, not their gender")

acadsPrior = input("Is academics & school the top priority for you? ")
if acadsPrior == "Y":
  print("Hello there, Ms. Granger!")

else:
  heroComplex = input("Do you have a thing of saving people, even if they are your lowkey bully? ")
  if heroComplex == "Y":
    print("Great to meet you, Mr. Harry James Potter!")

  else:
    marry = input("Did you marry your childhood crush? ")
    if marry == "Y":
      print("Hello, Mrs. Ginerva Weasley Potter")
    else:
      teacher = input("Have you been a teacher? ")
      
      if teacher == "Y":
        like = input("Do you like your profession? ")
        
        if like == "Y":
          print("Have a great day, Professor Lupin!")
          
        else:
          print("Hello, professor Snape!")
          

      else:
        ego = input("Are you an egoist? ")
        if ego == "Y":
          spoiled = input("Did you have a spoiled childhood? ")
          
          if spoiled == "Y":
            print("Hello Malfoy! Your father can't always help you out of your mess.")
           

          else:
            crazy = input("Are you a little crazy and violent tempered? ")
            if crazy == "Y":
              print("Hi Bellatrix! Goodbye")
              
            else:
              psycho = input("Do you consider yourself a psycho? ")
              if psycho == "Y":
                print("Hello, the one who should not be named. Let's call you Tom Riddle.")
              

        else:
          print("You aren't like any of these? Really 🙍‍♀️")
