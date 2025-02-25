# import sys
# sys.stdin = open("input.txt","r")

N,M = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for i in range(0,N-2):
    for j in range(1,N-1):
        for k in range(2,N):
            if arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k] and \
                ans <= arr[i]+arr[j]+arr[k] <= M:
                ans = arr[i]+arr[j]+arr[k]

print(ans)