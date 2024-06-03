# Day 56 Challenge

import csv
import os


print("⋆.˚✮🎧✮˚.⋆  Music Streaming Service  ⋆.˚✮🎧✮˚.⋆")
print()

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file) 
  
  for line in reader:
      
      song = line["Song"]
      artist = line["Artist(s)"]
    
      try:
        os.mkdir(artist)
      except:
        pass

      try:
        path = os.path.join(f"{artist}/", song)
        f = open(path,"w")
        f.close()

      except:
        pass

file.close()
