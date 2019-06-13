num1=int(input())
a=num1
b=0
while (num1>0):
  r=num%10
  b=b+(r**3)
  num1=num1//10
if a==b:
  print("yes")
else:
  print("no")  
