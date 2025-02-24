def abc(n):
    if n == 1:
        return 0
    for i in range(2, n-1):
        if n%i == 0:
            return 0
    return n

M = int(input())
N = int(input())
arr = []
for i in range(M, N+1):
    if abc(i):
        arr.append(i)
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))