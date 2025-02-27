lst1=list(map(int,input().split()))

for i in range(len(lst1)-3):
    for j in range(i+4):
        if j<len(lst1):
            print(lst1[j],end=" ")
    print()