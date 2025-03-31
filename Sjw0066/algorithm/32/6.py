N,M = map(int,input().split())
arr=[
    [] for _ in range(N)
]
for i in range(M):
    a,b=input().split()
    arr[int(a)].append(b)
Max=-21e8
Max_idx=0
for i in range(N):
    if Max<len(arr[i]):
        Max=len(arr[i])
        Max_idx=i
print(*arr[Max_idx])