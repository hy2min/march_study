n, m = map(int,input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sm = arr[i] + arr[j] + arr[k]
            if sm <= m and sm > ans :
                ans = sm

print(ans)