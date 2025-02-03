arr = [10, 50, 40, 20, 30, 40]

arr1 = list(map(int, input().split()))

for i in arr1:
    count = 0
    for j in arr:
        if i < j:
            count += 1
    print(f'{i}={count}개')