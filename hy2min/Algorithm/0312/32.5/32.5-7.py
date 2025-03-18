def find_size():
    for i in range(4):
        for j in range(8):
            total += arr[i][j]
    return total

mx = -21e8
arr = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for j in range(8):
        if arr[i][j] != 0:
            fin