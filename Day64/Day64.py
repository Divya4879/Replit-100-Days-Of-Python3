# Day 64 - OOPS

"""
class animal:
  name = None
  species = None
  sound = None
  # Sets the characteristics
  
  def __init__(self,name,species,sound):
    self.name = name
    self.species = species
    self.sound = sound
    # 'self' means 'this object'
    # This code sets the name, species and sound of each object to the arguments passed in when it is created (instantiated).

  def talk(self):
    print(f"{self.name} says {self.sound}!")

class bird(animal):
  color = None

  def __init__(self,color):
    self.name = "Chick"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class

cow = animal("Hari","Hybrid","Moo")
# Use the animal class to create a new object called 'cow' with the given parameters.
cow.talk()
# 'self' means 'use the identifier given to the object that is accessing this method'. 
# So If I use it with dog it will become 'dog.talk()' etc.


dog = animal("Rocky","German Shepherd","Woof")
dog.talk()

pigeon= bird("indigo")
pigeon.talk()

"""

# Fix the Code

# class animal:
#   species = None
#   name = None
#   sound = None

#   def __init__(self,name, species, sound):
#     self.name = name
#     self.species = species
#     self.sound = sound

#   def talk(self):
#     print((f"{self.name} says {self.sound}!"))

# class bird(animal):
#   color = None
  
#   def __init__(self,color):
#     self.name = "Bird"
#     self.species = "Avian"
#     self.sound = "Tweet"
#     self.color = color


# cow = animal("Ermintrude", "Bo Taurus", "Moo")
# print(cow.sound)
# cow.talk()

# polly = bird("Green") 
# polly.talk()
# print(polly.color)

# Day 64 Challenge

class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self,name,salary,hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def format_print(self):
    print()
    print("======================  JOB  ======================")
    print()
    print(f"{self.name:^15}{self.salary:^15}{self.hoursWorked:^15}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self,salary,hoursWorked,experience,speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def format_print(self):
    print()
    print("======================  JOB  ======================")
    print()
    print(f"{self.name:^11}{self.salary:^8}{self.hoursWorked:^6}{self.experience:^20}{self.speciality:^10}")

class teacher(job):
  subject = None
  position = None

  def __init__(self,salary,hoursWorked,subject,position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position

  def format_print(self):
    print()
    print("======================  JOB  ======================")
    print()
    print(f"{self.name:^11}{self.salary:^8}{self.hoursWorked:^6}{self.subject:^20}{self.salary:^10}")

print("           🌟Jobs Jobs Jobs!🌟\n")

lawyer = job("Lawyer","$ 90,000","60")
lawyer.format_print()

tech = teacher("$ 50,000","40","Computer Science","Teacher")
tech.format_print()

doc = doctor("$ 100,000","65","7 Years","Neurologist")
doc.format_print()
