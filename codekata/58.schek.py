p,q=map(int,input().split())
li=list(map(int,input().split()))
if len(li)==p:
  for i in li:
    if i==q:
      print("yes")
      break
  else:
    print("no")
