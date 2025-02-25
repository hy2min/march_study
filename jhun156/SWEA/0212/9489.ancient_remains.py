# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    Max = 0

    def find_x(y,x):
        cnt = 0
        if arr[y][x] == 1:
            while x <= m-1 and arr[y][x] == 1:
                x += 1
                cnt += 1
        return cnt

    def find_y(y,x):
        cnt = 0
        if arr[y][x] == 1:
            while y <= n-1 and arr[y][x] == 1:
                y += 1
                cnt += 1
        return cnt

    for i in range(n):
        for j in range(m):
            ans1 = find_y(i,j)
            ans2 = find_x(i,j)
            ans = max(ans1,ans2)
            if Max < ans:
                Max = ans
    print(f"#{tc} {Max}")