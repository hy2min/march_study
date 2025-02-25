arr = [
    ['A', 'B', 'K', 'T'],
    ['K', 'F', 'C', 'F'],
    ['B', 'B', 'Q', 'Q'],
    ['T', 'P', 'Z', 'F'],
]
a, b = input().split()
cnt = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] == a or arr[i][j] == b:
            cnt += 1

print(cnt)
