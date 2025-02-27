arr = [['A', 'T', 'K', 'B'], ['C', 'Z', 'F', 'D'], ['H', 'G', 'E', 'I']]

st, y, x = map(str, input().split())
y, x = int(y), int(x)

for i in range(3):
    for j in range(4):
        if arr[i][j] == st:
            st_num = arr[i+y][j+x]
print(st_num)