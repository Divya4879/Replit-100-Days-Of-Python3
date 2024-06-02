# Day 39 Challenge

import random,time,os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["suave", "integrity", "accent", "evil", "genius", "downtown","happy","development","ingenious","breathtaking","cajole","abject","acumen","colonel","nonplussed"]

while True:
  word = random.choice(word_list).lower()
  counter = 6
  letter_chosen = []
  for i in word:
    print("_",end ="")
  print()
  
  def view():
    for i in word:
      if i in letter_chosen:
        print(i,end = "")
      else:
        print("_",end = "")
    print()
  
  while True:
    

    word_list = list(word)
    print() 
    flag = 0
    if(all(x in letter_chosen for x in word_list)):
        flag = 1
    
    if (flag):
        print(f"Congrats🥳🪩🫧🫧✧˖°, you won with {counter} lives left!")
        exit()
    
    i = input("Choose a letter to find the word: ")
    
    if i in letter_chosen:
      print("You've tried that before!")
      if  counter <= 5:
        print(HANGMANPICS[6- counter])
      print()  
      
    elif i in word:
      print("Correct!")
      time.sleep(1.5)
      os.system("clear")
      letter_chosen.append(i)
      view() 
      
    else:
      print("Nope, not in there.")
      letter_chosen.append(i)
      counter -= 1
      if  counter <= 5:
        print(HANGMANPICS[6- counter])
      print()
      print(f"You have {counter} tries left.")
      time.sleep(1.5)
      os.system("clear")
      view()
      if counter == 0:
        print("You have no more tries left.You lost😭.")
        exit()
