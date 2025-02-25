# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    def check_omog(y,x):
        down, right, down_right,up_right = 0,0,0,0
        if arr[y][x] != 'o':
            return 0
        else:
            y1,x1 = y,x
            while y1 <= N -1 and x1 <= N -1 and arr[y1][x1] == 'o':
                y1 += 1
                x1 += 1
                down_right += 1
                if down_right == 5:
                    break
            y2,x2 = y,x
            while y2 <= N -1 and arr[y2][x2] == 'o':
                y2 += 1
                down += 1
                if down == 5:
                    break
            y3,x3 = y,x
            while x3 <= N -1 and arr[y3][x3] == 'o':
                x3 += 1
                right += 1
                if right == 5:
                    break
            y4,x4 = y,x
            while x4 <= N -1 and y4 >= 0 and arr[y4][x4] == 'o':
                x4 += 1
                y4 -= 1
                up_right += 1
                if up_right == 5:
                    break
        if max(down,right,down_right,up_right) == 5:
            return 1
        else:
            return 0

    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = check_omog(i,j)
            ans += tmp

    if ans > 0:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")