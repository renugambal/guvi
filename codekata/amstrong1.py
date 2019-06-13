a=int(input())
t=a
b=0
while (a>0):
  r=a%10
  b=b+(r**3)
  a=a//10
if b==t:
  print("yes")
else:
  print("no")  
