arr = list(map(int,input().split()))

for i in range(4):
    for j in range(0,i+4):
        print(arr[j],end=' ')
    print()

