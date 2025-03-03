def func(arr):
    cnt = 0
    for lst in arr:
        for i in range(1,len(lst)):
            if lst[i-1] != lst[i]:
                cnt += 1
    return cnt

n = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(n):
    y,x = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            arr[i][j] = 1

arr_t = list(zip(*arr))
ans = func(arr) + func(arr_t)
print(ans)