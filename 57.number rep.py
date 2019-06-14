i,j=map(int,input().split())
l=list(map(int,input().split()))
c=0
if len(l)==i:
  for a in l:
    if a==j:
      c=c+1
  print(c)
