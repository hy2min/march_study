arr = [list(input()) for _ in range(4)]

arr2 = [
    ['A', 'B', 'C', 'D'],
    ['B', 'B', 'A', 'B'],
    ['C', 'B', 'A', 'C'],
    ['B', 'A', 'A', 'A'],
]

cnt = [0,0,0,0]

for i in range(4) : 
    for j in range(4) : 
        if arr[i][j] == arr2[i][j] : 
            cnt[ord(arr[i][j])-65] += 1

ans = chr(cnt.index(max(cnt))+65)
print(ans)