y=int(input())
sum=0
while(y>0):
  r=y%10
  sum=sum+(r**2)
  y=y//10
print(sum)
