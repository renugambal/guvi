s=int(input())
lis=list(map(int,input().split()))
if len(lis)==s:
  for i in range(s):
    print(lis[i],i)
