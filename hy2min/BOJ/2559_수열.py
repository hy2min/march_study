n, k = map(int, input().split())
arr = list(map(int, input().split()))
sm = sum(arr[:k])
mx = sm
for i in range(k,n):
    sm  = sm + arr[i]-arr[i-k]
    if mx < sm:
        mx = sm
print(mx)