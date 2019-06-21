n,k=map(int,input().split())
pq=list(map(int,input().split()))
if pq[k]%2!=0:
  print(pq[k])
else:
  print(pq[k-1])
