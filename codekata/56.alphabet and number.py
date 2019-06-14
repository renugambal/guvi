st=input()
a=False
b=False
for i in st:
  if i.isalpha():
    a=True
  if i.isdigit():
    b=True
if a==True and b==True:
  print("Yes")
else:
  print("No")
