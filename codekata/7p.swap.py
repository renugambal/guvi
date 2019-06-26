a=input()
l=[a[i] for i in range(len(a)) if i%2==0]
l1=[a[i] for i in range(len(a)) if i%2!=0]
for j in range(len(a)//2):
  print(l1[j]+l[j],end="")

