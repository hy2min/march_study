def search(y, x):
    Sum = 0
    start = x
    end = x
    for i in range(start+1, 8):
        if arr[y][i]:
            end = i
        else:
            break

    for i in range(y, 4):
        row = arr[i][start:end + 1]
        if 0 not in row:
            Sum += sum(row)
        else:
            break

    return Sum

arr = [list(map(int, input().split())) for _ in range(4)]
Max = 0
for i in range(4):
    for j in range(8):
        if arr[i][j]:
            Max = max(Max, search(i, j))
print(Max)