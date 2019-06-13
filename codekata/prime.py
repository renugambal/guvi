dig=int(input())
if dig>1:
  for i in range(2,dig):
    if dig%i==0:
      print("no")
      break
  else:
    print("yes")
else:
  print("no")   
