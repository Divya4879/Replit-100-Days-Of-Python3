# Day 90 Challenge

import requests

for i in range(10):
  result = requests.get("https://randomuser.me/api/") 
  
  if result.status_code == 200:
    
    users = result.json()
      
    name = f"""{users["results"][0]["name"]["first"].lower()} {users["results"][0]["name"]["last"].lower()}"""
    
    picture = f"""{users["results"][0]["picture"]["large"]}"""
    
    picture = requests.get(picture)
    
    f = open(f"{name}.jpg","wb")
    
    f.write(picture.content) 
    f.close()
    print(f"Saved {name}.jpg!")
