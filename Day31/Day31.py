# Day 31 Challenge
import time
def colors_spaces(color):
  if color=="red":
    return "\033[31m"
  elif color=="blue":
    return "\033[34m"
  elif color=="green":
    return "\033[32m"
  elif color=="purple":
    return "\033[35m"
  elif color=="cyan":
    return "\033[36m"
  elif color=="dark_gray":
    return "\033[1;30m"
  elif color=="yellow":
    return "\033[1;33m"
  elif color=="light_green":
    return "\033[1;32m"
  elif color=="light_purple":
    return "\033[1;35m"
  else:
    return "\033[0m"

title = f"{colors_spaces('red')}={colors_spaces('white')}={colors_spaces('blue')}= {colors_spaces('yellow')}Music App {colors_spaces('blue')}={colors_spaces('white')}={colors_spaces('red')}="
print(f"              {title:^40}")

print()
print()
line1 = "Radio Gaga"
line2 = "Queen"

print(f"🔥🎧{colors_spaces('white')}{line1 : >15}")

print(f"{colors_spaces('yellow')}{line2 : >14}",end="\n\n\n")

print(f"{colors_spaces('white')} PREV")

colors_spaces("light_green")
text = "NEXT"
print(f"{colors_spaces('green')}{text : >10}")

text = "PAUSE"
print(f"{colors_spaces('red')}{text : >17}")



print()
print("",end="\n\n\n\n\n")
time.sleep(5)
text = "WELCOME TO"
print(f"{colors_spaces('white')}{text : ^40}")

text = "--    ARMBOOK    --"
print(f"{colors_spaces('blue')}{text :^40}")

print("",end="\n\n")

text = "Definitely not a rip off of"
print(f"{colors_spaces('yellow')}{text :>42}")

text = "a certain other social"
print(f"{colors_spaces('yellow')}{text :>42}")

text = "networking site."
print(f"{colors_spaces('yellow')}{text :>42}")

print()

text = "Honest."
print(f"{colors_spaces('red')}{text:^40}")
print()

text = "Username:"
print(f"{colors_spaces('white')}{text:^40}")
text = "Password:"
print(f"{colors_spaces('white')}{text:^40}")
