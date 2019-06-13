n=int(input())
a=n
b=0
while (n>0):
  r=n%10
  b=b+(r**3)
  n=n//10
if a==n:
  print("yes")
else:
  print("no")  
