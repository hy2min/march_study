def backtracking(idx):
    global max_total, total
    if max_total > total:
        return
    if max_total < total:
        max_total = total
        return
    total += arr[idx]
    arr[idx] = 0
    if idx >= 1:
        arr[idx-1] = 0
    if idx < n-1 :
        arr[idx+1] = 0

    for i in range(n):
        if arr[i] != 0:
            backtracking(idx+1)

n = int(input())
arr = list(map(int, input().split()))
max_total = -21e8
total = 0
backtracking(0)
print(max_total)