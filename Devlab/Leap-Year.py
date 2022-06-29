a = int(input())
if a % 4 == 0:
  if a % 400 == 0:
  	print("Leap Year")
  elif a % 100 == 0:
  	print("Not a Leap Year")
  else:
    print("Leap Year")
else:
  print("Not a Leap Year")