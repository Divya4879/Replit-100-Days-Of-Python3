# Day 65 Challenge
import datetime

class character:
  name = None
  health = None
  magicPoints = None

  def __init__(self,name,magicPoints):
    self.name = name
    self.health = 100
    self.magicPoints = magicPoints

class player(character):
  nickname = None
  lives = 3

  def __init__(self,nickname,magicPoints):
    self.name = "Player"
    self.health = 100
    self.magicPoints = magicPoints
    self.nickname = nickname
    self.lives = 3 

  def amIAlive(self):
    if self.lives and self.lives > 0:
      return (f"{self.nickname} lives on!")

  def format_print(self):
    print(f"""{self.name:>11}:\tHealth: {self.health:<4}\tM.P: {self.magicPoints:<4}\tNickname: {self.nickname:^20}\t\tLives: {self.lives:<3}\t\t{self.amIAlive()}""")
    
class enemy(character):
  type = None
  strength = None

  def __init__(self,type,strength,magicPoints):
    self.type = type
    self.strength = strength
    self.magicPoints = magicPoints

class orc(enemy):
  speed = None

  def __init__(self,name,strength,speed,magicPoints):
    self.health = 100
    self.name = name
    self.magicPoints = magicPoints
    self.type = "Orc"
    self.strength = strength
    self.speed = speed

  def format_print(self):
    print()
    print(f"""{self.name:>11}:\tHealth: {self.health:>4}\tM.P: {self.magicPoints:<4}\tType: {self.type:^20}\t\tStrength: {self.strength:<3}\t\tSpeed: {self.speed}""")


class vampire(enemy):
  dayOrNight = True

  def __init__(self,name,strength,magicPoints):
    
    self.type = "Vampire"
    self.magicPoints = magicPoints
    self.health = 100
    self.strength = strength
    self.name = name
    self.dayOrNight = True
    timeNow = str(datetime.datetime.now()).split(" ")    
    timeNow = int(timeNow[1].split(".")[0][:2])
    
    if 5>timeNow>18:
      self.dayOrNight = False

  def format_print(self):
    print()
    print(f"""{self.name:>11}:\tHealth: {self.health:<4}\tM.P: {self.magicPoints:<4}\tType: {self.type:^20}\t\tStrength: {self.strength:<3}\t\tDay?: {self.dayOrNight}""")


Harry = player("The Boy Who Lives",50)
vamp1 = vampire("Dracula",150,80)
vamp2 = vampire("Salvatore",125,60)
Orc1 = orc("Orcus",160,80,40)
Orc2 = orc("Morcus",150,70,35)
Orc3 = orc("Dorcus",165,60,50)

title = "🤺⚔️🗡️ Divya RPG 🤺⚔️🗡️"
print(f"{title:^140}\n\n")
Harry.format_print()
vamp1.format_print()
vamp2.format_print()
Orc1.format_print()
Orc2.format_print()
Orc3.format_print()
