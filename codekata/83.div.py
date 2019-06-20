p=input()
for i in p:
  if i=='/':
    c=p.split('/')
    print(int(int(c[0])/int(c[1])))
  elif i=='%':
    c=p.split('%')
    print(int(int(c[0])%int(c[1])))
