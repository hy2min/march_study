# import sys
# sys.stdin = open("input.txt","r")

def dfs(battery,cnt,index):     # 현재 내 배터리, 카운트, 인덱스

    global ans
    if cnt > ans:
        return
    if battery == 0:
        return
    if index + battery >= goal:     # 현재 내 인덱스 + 배터리 >= 목표지점인덱스
        ans = min(cnt,ans)
        return

    dfs(arr[index+1],cnt+1,index+1) # 전진하고 교체한 경우
    dfs(battery-1,cnt,index+1)  # 전진하고 교체하지 않은 경우


T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr.pop(0)
    ans = 21e8
    goal = N - 1    # 골인지점 인덱스

    dfs(arr[0],0,0)
    print(f"#{tc} {ans}")