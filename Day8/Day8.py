# Motivational and Inspirational Application

print("This is a simple positivity quote generator built for you 😊")
print()

print("First of all, let me ask you a few questions to get to know you.")
name = input("What's your first name? ").capitalize()


goal = input("Name the one thing you want to get good at for your better tomorrow: ")

rate = int(input("On a scale of 1-10, how do you feel right now? (1 = 😢 and 10 = 😁) "))
print()

if rate == 1:

  print(f"Dear {name}, I'm really sad to know that. Please take care of yourself, rest, physical exercise, meditation, journal. Not only journalling helps us write down all our thoughts and feelings & let us introspect on them, but it's also proven that maintaining a Gratitude journal helps us being more grateful for what we have and improves our mood as well.")
  print("")
  print("Please know that you're good enough, you're smart enough, you're resilient to enough to get out of your current circumstances, remember all those times you proved yourself and others wrong by your achievements, you can also do it!")
  print()
  print(f"So now is the time to rise up above your circumstances, relax and recharge yourself, take up small daily challenges to rebuild your confidence in yourself, improve your physical & mental health, do {goal} everyday, even if it's just 30 mins, and there will be results, I can promise you that. Now, put a smile on that face of yours, and let's get to work!!")


if rate == 10:
  print(f"Woah! That's amazing {name} I am glad to know that! Work hard on {goal}, I sincerely hope you stay happy & I wish you a great day!😁")


if rate >= 2 and rate <= 9:
  burnOut = input("Is burn-out the main culprit? (Reply as 'y' or 'n')")
  if burnOut == "y":
    print(f"{name}, you need some rest my friend! I would suggest a trip to somewhere you've always wanted to go or atleast a weekend getaway with no work, spend time with your loved ones, prioritise yourself and take care of yourself by exercising, journaling, meditation, or whatever you need.")
    print()
    print(f"I really hope you take care of yourself and take it easy on yourself. Rememeber, life is a marathon and not a sprint. Also, spend some time on {goal} coz you know you have always wanted to get better at it, not for others and under any obligations, but just for yourself!")

  else:
    selfWorth = input("Is lack of self-worth the main culprit? (Reply as 'y' or 'n')")
    if selfWorth == "y":
      print(f"Please always remember {name} that you're worth it, whether it was yesterday, today, or tomorrow! Don't let others or even you, yourself make you believe it otherwise. If it's others, please don't let them get to you, they're not worth it.")
      print()
      print(f"If you really believe you need to level up, just strategize and get to it! Rem ember your wish of getting better at {goal}, get to it. Set aside at the very least half an hour a day to work on it. There's no overnight success, but trust yourself, there will be profound changes in even a month!!")

    else:
      stuck = input("Is it feeling stuck despite trying your best that has got you down? (Reply as 'y' or 'n')")
      if stuck == "y":
        print(f"Alrighty then {name}, do you really not feel as if you achieved anything by your consistent, dedicated efforts or is it that you're unable to reach an over-ambitious goal for yourself that you feel like you can't achieve? Or is it perhaps that you're comparing yourself with an overachiever who just seems perfect?")
        print()
        print(f"Please remember to have trust in yourself and yup, you gotta trust the process. Please just enjoy this journey for now, don't overexert yourself and keep working hard for your {goal}. Remember, you have already come so far, and yup, 'Good things take time!'")


      else:
        worried = input("Are you worried about something, and that's the main culprit? (Reply as 'y' or 'n')")
        if worried == "y":
          print(f"Hey {name}! Please know that you're stronger than your circumstances, and not only can you overcome your current circumstances, but you are gonna crush it. It's ok to be a little worried/ stressed/ feel like an imposter, but you've already came this far, and you're meant to go much further!")
          print()
          print(f"Keep your chin high, put a smile on your face, believe in yourself, and work hard towards your {goal}. You got this 🥰")

        else:
          print(f"Dear {name}, prioritize your self, your physical & mental well-being, your goals of getting better at {goal} (or perhaps perfecting it), your loved ones, friends, relatives. Please know that whatever you want is within your reach.")
          print()
          print("I wanna share something with you. 'The harder I work, the luckier I get!'")


print()
print("I sincerely wish that I was able to help you, however miniscule it might be, but remember you're the only one who can truly help themselves.")
