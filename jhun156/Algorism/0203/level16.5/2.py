a = ord('A')
arr = [[0] * 3 for _ in range(6)]

for i in range(3):
    for j in range(6):
        arr[5-j][2-i] = chr(a)
        a += 1

x,y = map(int,input().split())
print(arr[x][y])