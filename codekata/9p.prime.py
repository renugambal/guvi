a,b=map(int,input().split())
l=[]
c=0
for i in range(a,b+1):
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      l.append(i)
print(len(l))
