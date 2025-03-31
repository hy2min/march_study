def solve():
    N= 9
    num = sum(arr)-100
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i]+ arr[j] == num:
                return arr[i],arr[j]

arr = [int(input()) for _ in range(9)]
n,m = solve()
for i in sorted(arr):
    if i!=n and i!=m:
        print(i)



