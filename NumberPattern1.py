a=int(input())

for k in range(1,a+1):
  for i in range(1,a+1):
    if i<=k:
      print(i,end=" ")
    else:
      print(" ",end=" ")
  for i in range(a,0,-1):
    if i<=k:
      print(i,end=" ")
    else:
      print(" ",end=" ")
  print()    
