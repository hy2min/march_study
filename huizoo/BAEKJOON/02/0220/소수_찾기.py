n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    flag = 0
    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            flag = 1
    if not flag:
        cnt += 1
if 1 in arr:
    print(cnt-1)
else:
    print(cnt)