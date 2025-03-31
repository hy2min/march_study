lst1=list(map(str,input().split()))

for i in range(5):
    for j in range(i,5):
        print(lst1[j],end=" ")
    print()