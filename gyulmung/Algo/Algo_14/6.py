vect = [3, 5, 1, 1, 2, 3, 2]
arr = list(map(int, input().split()))

for i in arr:
    count=0
    for j in vect:
        if i == j:
            count += 1
    print(f'{i}={count}개')