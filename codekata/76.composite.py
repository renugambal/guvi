w=int(input())
if w>1:
    for i in range(2,w):
        if w%i==0:
            print("yes")
            break
    else:
        print("no")
