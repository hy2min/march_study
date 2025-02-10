arr=list(map(int,input().split()))
for i in range(4):
    for j in range(i+4):
        print(arr[j],end=' ')
    print()