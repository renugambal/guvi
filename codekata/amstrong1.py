num=int(input())
a=num
b=0
while (num>0):
  r=num%10
  b=b+(r**3)
  num=num//10
if a==b:
  print("yes")
else:
  print("no")  
