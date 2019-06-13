nu=int(input())
a=list(map(int,input().split()))
if len(a)==nu:
  a.sort()
for i in range(nu):
  print(a[i],end=" ")
