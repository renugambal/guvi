o=int(input())
r,s=map(int,input().split())
for i in range(r+1,s):
  if o==i:
    print("yes")
    break
else:
  print("no")
