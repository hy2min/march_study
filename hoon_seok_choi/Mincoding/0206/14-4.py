arr = list(map(str, input().split()))


for i in range(5) :
    for j in range(5-i) :
        print(arr[j+i], end=" ")
    print()

