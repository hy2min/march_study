arr = [[0]*4 for _ in range(7)]
for i in range(7):
    for j in range(4):
        arr[i][j] = 4*i+j + 1

a, b, c = map(int, input().split())
arr[a] = [0]*4
arr[b] = [0]*4
arr[c] = [0]*4

print('\n'.join(' '.join(map(str, row)) for row in arr))