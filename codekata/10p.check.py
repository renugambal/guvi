s1,s2=map(str,input().split())
c=0
if len(s1)==len(s2):
  for i in range(len(s1)):
    if s1[i]==s2[i]:
      print("yes")
      break
  else:
    print("no")  
      
