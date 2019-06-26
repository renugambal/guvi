num=int(input())
string=list(input())
l=['a','A','e','E','i','I','o','O','u','U']
for i in string:
  if i in l:
    string.remove(i)
s=string[::-1]
for i in range(len(s)):
  print(s[i],end="")
