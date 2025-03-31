arr = [0] * 5

for i in range(5):
    for j in range(1):
        person = list(map(int, input().split()))
        arr[i] = person

for i in range(5):
    count = 0
    for j in range(4):
        count += arr[i][j]
    print(count, end = " ")