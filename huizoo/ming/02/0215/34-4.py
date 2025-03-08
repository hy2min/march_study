N = int(input())
arr = [list(input()) for _ in range(N)]
y, x = 0, 0
while y < N:
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if arr[y][mid] == '#':
            x = mid
            start = mid+1
        elif arr[y][mid] == '0':
            end = mid-1
    if mid == N-1:
        y += 1
    else:
        break
print(y, x)