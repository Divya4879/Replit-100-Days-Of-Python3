# Day 63 Code

# import test as tt 
# # No need for the .py

# tt.countdown()

# Fix The Code

# import test as tt

# print("Countdown")
# tt.countdown()

# Day 63 Challenge
import os,time
import Divya_library as dl


li = dl.colors.keys()
dl.pretty_print_colors(li)
  
new_list = input("Wanna create a new list?(y/n): ").strip().lower()[0]
print()
if new_list == "y":
  dl.create_list()

new_dict = input("Wanna create a new dict ?(y/n): ").strip().lower()[0]
print()
if new_dict == "y":
  dl.create_dict()


new_2dList = input("Wanna create a new 2D-List?(y/n): ").strip().lower()[0]
print()
if new_2dList == "y":
  dl.add_2dList()
