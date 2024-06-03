# Day 59 Challenge

print("🌟Palindrome Checker🌟")
print()

word = input("Input a word > ").lower()

def palindrome(str):
  if len(str) <= 1:
    return True

  elif str[0] != str[-1]:
    return False
  
  return palindrome(str[1:-1])

if palindrome(word) == True:
  print(f"{word} is a palindrome.\nYay!")

else:
  print(f"{word} isn't a palindrome!") 
