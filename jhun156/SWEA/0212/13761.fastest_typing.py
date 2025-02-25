# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    n,k = len(arr[0]),len(arr[1])
    cnt = n
    for i in range(n-k+1):
        if arr[0][i:i+k] == arr[1]:
           cnt -= (k-1)

    print(f"#{tc} {cnt}")