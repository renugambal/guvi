o=int(input())
r,s=map(int,input().split())
for i in range(r,s+1):
  if o==i:
    print("yes")
    break
else:
  print("no")
