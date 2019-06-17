f=int(input())
if f>1:
    for i in range(2,f):
        if f%i==0:
            print("no")
            break
    else:
        print("yes")
