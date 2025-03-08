arr = list(map(int, input().split()))
for i in range(4):
    for j in range(4+i):
        print(arr[j], end=' ')
    print()