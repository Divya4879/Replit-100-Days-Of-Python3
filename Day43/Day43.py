import random
print("A Bingo Card Generator for your grandparents",end = "\n\n\n")

bingoList=[]
bingo = [[],[],[],[],[]]
while len(bingoList) < 25:
   r=random.randint(1,89)
   if r not in bingoList:
      bingoList.append(r)

bingoList.sort()
    
for i in range(5):
  bingo[i] = bingoList[:5]
  del bingoList[:5]
  
bingo[2][2] = "BINGO"

for i in range(5):
  for j in range(5):
    if j == 2:
      print(f"{bingo[i][j] :^5}",end =" | ")
    elif j == 4:
      print(f"{bingo[i][j]:^2}",end ="")
    else:
      print(f"{bingo[i][j]:^2}",end =" | ")

  
 
  print()
  if i <4:
    print("-------------------------")
