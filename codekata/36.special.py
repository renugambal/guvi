a=input()
c=0
for j in a:
  if j.isalpha()!=True and j.isdigit()!=True and j!=" ":
    c=c+1
print(c)
