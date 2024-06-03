# Day 66

# window = tk.Tk()
# window.title("Hello") # Sets the name of the window in the border
# window.geometry("400x400") # Sets the size of the window in pixels

# label = "Hola folks!"

# def updateLabel():
#   label = "Bye world!"
#   hello["text"] = label 
#   # Subroutine that updates the text in the label.

# hello = tk.Label(text = label)
# # hello = tk.Label(text = "Hello World") # Creates a text box
# hello.pack() # 'pack' places the element on the screen

# button = tk.Button(text = "Wanna see something cool?", command = updateLabel) 
# # Creates a button
# button.pack()

# tk.mainloop()

# Incrementing label

# window = tk.Tk()
# window.title("Hello World") 
# window.geometry("300x300") 

# label = 0 # Sets the starting label value to 0

# def updateLabel():
#   global label # Uses the values in the label variable
#   label += 1 # Adds one to the value in the label
#   hello["text"] = label 


# hello = tk.Label(text = label) 
# hello.pack() 

# button = tk.Button(text = "Click me!", command = updateLabel) # Calls the updateLabel subroutine when the button is clicked
# button.pack()

# tk.mainloop()

# window = tk.Tk()
# window.title("Hello World") 
# window.geometry("300x300") 

# label = 0

# def updateLabel():
#   global label
#   number = text.get("1.0","end") # Gets the number from the text box (starting at the first position and going to the end.) and stores in the number variable
#   number = int(number) #Casts to an integer. I've done this on a separate line to prevent the line above getting too complex, but you can combine the two.
#   label += number # Adds the number from the text box to the one in the label.
#   hello["text"] = label


# hello = tk.Label(text = label) 
# hello.pack() 


# text = tk.Text(window ,height=1, width = 50)
# text.pack()

# # button = tk.Button(text = "Click me!", command = updateLabel) 
# # button.pack(side=tk.BOTTOM)

# button = tk.Button(text = "Click me!",
# command = updateLabel) 
# button.pack()

# button = tk.Button(text = "Another Button", command = updateLabel) 
# button.pack()

# button = tk.Button(text = "Last one", command = updateLabel) 
# button.pack()

# tk.mainloop()

# window = tk.Tk()
# window.title("Hello World") 
# window.geometry("800x500") 

# label = 0

# def updateLabel():
#   global label
#   number = text.get("1.0","end") 
#   number = int(number) 
#   label += number
#   hello["text"] = label 


# hello = tk.Label(text = label).grid(row=0, column=1)


# text = tk.Text(window ,height=1, width = 50).grid(row=1, column=1)


# button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

# button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

# button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

# tk.mainloop()

# pack doesn't work with grid. You have to decide to use one or the other.

# window = tk.Tk()
# window.title("Hello World") 
# window.geometry("800x300") 

# label = 0

# def updateLabel():
#   global label
#   number = text.get("1.0","end") 
#   number = int(number) 
#   label += number
#   hello["text"] = label 


# hello = tk.Label(text = label)
# hello.grid(row=0, column=1) # New line here

# text = tk.Text(window ,height=1, width = 50)
# text.grid(row=1, column=1) # New line here

# button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

# button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

# button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

# tk.mainloop()

# Fix the Code

"""

window = tk.Tk()
window.title("Hello World") 
window.geometry("800x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 


hello = tk.Label(text = label).grid(row=0, column=1)

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) # New line here

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()

"""

# Day 66 Challenge

import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator") 
window.geometry("600x400") 


res = 0
noChosen = 0
operator = None

def typeRes(val):
  global res
  res = f"{res}{val}"
  res = int(res)
  hello["text"] = res

def calcRes(op):
  global res, noChosen, operator
  noChosen = res
  res = 0
  if op == "+":
    operator = "+"
  elif op == "-":
    operator = "-"
  elif op == "*":
    operator = "*"
  elif op == "/":
    operator = "/"
  hello["text"] = res

def calc():
  global res, noChosen, operator
  total = res
  print(f"{noChosen}\t{res}\t{operator}")
  if operator == "+":
    total = noChosen + int(res)
  elif operator == "-":
    total = noChosen - int(res)
  elif operator == "*":
    total = noChosen * int(res)
  elif operator == "/":
    total = noChosen / int(res)
  res = total
  hello["text"] = res

hello = tk.Label(text = res)
hello.grid(row=0, column=2) 


button = tk.Button(text = 1, command = lambda:typeRes(1))
button.grid(row=1, column=0)

button = tk.Button(text = 2, command = lambda:typeRes(2))
button.grid(row=1, column=1)

button = tk.Button(text = 3, command = lambda:typeRes(3))
button.grid(row=1, column=2)

button = tk.Button(text = 4, command = lambda:typeRes(4))
button.grid(row=2, column=0)

button = tk.Button(text = 5, command = lambda:typeRes(5)) 
button.grid(row=2, column=1)

button = tk.Button(text = 6, command = lambda:typeRes(6))
button.grid(row=2, column=2)

button = tk.Button(text = 7, command = lambda:typeRes(7))
button.grid(row=3, column=0)

button = tk.Button(text = 8, command = lambda:typeRes(8))
button.grid(row=3, column=1) 

button = tk.Button(text = 0, command = lambda:typeRes(0))
button.grid(row=4, column=1)

button = tk.Button(text = 9, command = lambda:typeRes(9))
button.grid(row=3, column=2)

button = tk.Button(text = "+", command = lambda:calcRes("+")).grid(row=1, column=3)

button = tk.Button(text = "-", command = lambda:calcRes("-"))
button.grid(row=1, column=4)  

button = tk.Button(text = "*", command = lambda:calcRes("*"))
button.grid(row=2, column=3)

button = tk.Button(text = "/", command = lambda:calcRes("/"))
button.grid(row=2, column=4)

button = tk.Button(text = "=", command = calc)
button.grid(row=4, column=3) 

tk.mainloop()
