k=input()
l=list(k)
a=len(l)//2
if len(l)%2==0:
  l[a]='*'
  l[a-1]='*'
else:
  l[a]='*'
for i in range(len(l)):
  print(l[i],end="")
