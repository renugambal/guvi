n1,n2=map(str,input().split())
if len(n1)!=len(n2):
  print("no")
xx=[n1.count(ch) for ch in n1]
yy=[n2.count(ch) for ch in n2]
if(xx==yy):
  print("yes")
else:
  print("no")
