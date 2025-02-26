arr = [[0]*3 for i in range(6)]
count = 0
for i in range(2, -1 , -1):
    for j in range(5, -1, -1):
        arr[j][i] = chr(ord('A')+count)
        count += 1
a, b = map(int, input().split())
print(arr[a][b])