a,b,c = map(str,input().split())
a,b = int(a), int(b)

for i in range(2) :
    for j in range(a) :
        for k in range(b) :
            print(c,end="")
        print()
    print()

