a,b=map(int,input().split())
for i in range(a+1,b):
  t=i
  d=0
  while (i>0):
    r=i%10
    d=d+(r**3)
    i=i//10
  if t==d:
    print(d,end=" ")
