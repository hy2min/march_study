# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    n = len(arr1)
    m = len(arr2)
    if n > m:
        ans = -1000
        for i in range(n-m+1):
            mul_sum = 0
            for j in range(m):
                mul_sum += arr2[j] * arr1[j+i]
            if mul_sum > ans:
                ans = mul_sum
    else:
        ans = -1000
        for i in range(m-n+1):
            mul_sum = 0
            for j in range(n):
                mul_sum += arr1[j] * arr2[i+j]
            if mul_sum > ans:
                ans = mul_sum

    print(f"#{tc} {ans}")