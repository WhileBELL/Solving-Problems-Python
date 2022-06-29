a = int(input())
for x in range(1,a+1):
  for y in range(a - x):
    print(" ",end="")
  for y in range(1,x + 1):
    print("*",end="")
  for y in range(2,x + 1):
    print("*",end="")
  print()