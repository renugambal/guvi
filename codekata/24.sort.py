num=int(input())
p=list(map(int,input().split()))
if len(p)==num:
  p.sort()
for i in range(num):
  print(p[i],end=" ")
