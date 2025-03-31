P = int(input())
N = int(input())

for _ in range(N):
    P *= 2
    arr = []
    while True:
        arr.append(P % 10)
        P //= 10
        if P == 0:
            break
    ans = 0
    n = len(arr)
    for i in range(n):
        ans += arr[i] * (10 ** (n-1-i))
    P = ans

print(P)