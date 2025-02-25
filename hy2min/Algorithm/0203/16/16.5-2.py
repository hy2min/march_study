arr = [[0]* 3 for _ in range(6)]
start = 65
for i in range(3):
    for j in range(6):
        arr[5-j][2-i] = chr(start)
        start += 1

a, b = map(int, input().split())
print(arr[a][b])