# import sys
# sys.stdin = open("input.txt","r")

def find_cost(level,Sum):

    global ans
    if level == N:
        ans = min(ans,Sum)
        return

    for i in range(N):
        if used[i] == 0:
            if Sum + cost_arr[level][i] > ans:
                continue
            used[i] = 1
            find_cost(level+1,Sum+cost_arr[level][i])
            used[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cost_arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N
    ans = 21e8

    find_cost(0,0)
    print(f"#{tc} {ans}")