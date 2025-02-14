lst  = list(map(int, input().split()))
result_arr = [[0]*4 for _ in range(4)]

arr =[]
cnt = 1
for i in range(4):
    inner_arr = []
    for j in range(4):
        inner_arr.append(cnt)
        cnt += 1
    arr.append(inner_arr)
print(arr)

def find_PW(y,x):
    for i in range(4):
        if arr[y][x] == lst[i]:
            return y, x
    return 0, 0

y, x = 0, 0
count = 1
for i in range(4):
    for j in range(4):
        for k in range(4):
            if arr[i][j] == lst[k]:
                arr[i][j] == count
                count += 1
            else:
                arr[i][j] = 0
        

print(arr)