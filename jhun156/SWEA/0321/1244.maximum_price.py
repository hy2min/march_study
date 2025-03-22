# import sys
# sys.stdin = open("input.txt","r")

def dfs(level):

    global ans
    if level == N:
        price = 0
        for i in range(L):
            price += arr[i] * (10 ** (L-1-i))
        ans = max(ans,price)
        return

    # 중복체크
    arr_tuple = tuple(arr)
    if arr_tuple in check:
        return
    check.add(arr_tuple)

    # 탐색
    for i in range(L):
        for j in range(L):
            if i == j:
                continue
            arr[i],arr[j] = arr[j],arr[i]
            dfs(level+1)
            arr[i], arr[j] = arr[j], arr[i] # 원상복구


T = int(input())
for tc in range(1,T+1):
    tmp, N = input().split()
    N = int(N)
    arr = list(map(int,tmp))
    L = len(arr)
    ans = 0
    check = set()

    dfs(0)
    print(f"#{tc} {ans}")