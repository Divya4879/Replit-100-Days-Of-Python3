"""
# Day 26 Code

import os
import time

print("Welcome")
print("to")
print("Replit")
time.sleep(3)
os.system("clear")

username = input("Username: ")

"""

# Day 26 Challenge

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  
  while True:
    # Start taking user input and doing something with it
    stop_music = input("Press 2 anytime if you want to stop this music and return back to the main menu ")
    
    print("Playing a soothing music for you!")

    if stop_music == "2":
      source.paused = True
      break

    

while True:
  os.system("clear")
  print("🎵 MyRelax Music Player")
  print()
  time.sleep(2)
  print("Press 1 to play")
  time.sleep(1)
  print("Press 2 to exit")
  time.sleep(1)
  print("Press anything else to see the menu again: ")
  time.sleep(1)
  
  user_prompt = input("")
  
  
  if user_prompt == "1":
    play()

  elif user_prompt == "2":
    exit()

  else:
    continue
