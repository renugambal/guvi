num=int(input())
a=0
b=1
while num:
  print(b,end=" ")
  a,b=b,a+b
  num=num-1
