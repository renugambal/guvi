s=int(input())
li=list(map(int,input().split()))
if len(li)==s:
  li.sort()
  print(li[len(li)//2])
