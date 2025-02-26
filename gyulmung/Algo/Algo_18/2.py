lst = [list(map(int, input().split())) for _ in range(3)]
arr = [0]*10
not_arr = []

for i in range(3):
    for j in range(3):
        arr[lst[i][j]] += 1

for i in range(1, 10):
    if arr[i] == 0:
        not_arr.append(i)

print(*not_arr)