x,y=map(int,input().split())
lis=list(map(int,input().split()))
sum=0
if len(lis)==x:
  for i in range(len(lis)+1):
    if i<y:
      sum=sum+lis[i]
  print(sum)
