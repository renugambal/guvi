s=input()
if any(a.isalpha() for a in s):
  print("No")
elif any(a.isdigit() for a in s):
  print("yes")  
