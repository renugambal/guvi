so=list(input())
p=[]
for i in so:
    if i not in p:
        p.append(i)
if so==p:
    print("Yes")
else:
    print("No")
