# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    def Matryoshka(y,x,length,num):

        if num % 2 == 0:
            m = num // 2
            up = y - m + 1
            down = y + m
            right = x + m
            left = x - m + 1
            if up >= 0 and down <= length -1:
                cnt = 0
                for i in range(m):
                    if arr[y+1+i][x] == arr[y-i][x]:
                        cnt += 1
                if cnt == m:
                    return ['x',y-m+1,y+m+1]
            if right <= length - 1 and left >= 0:
                cnt = 0
                for i in range(m):
                    if arr[y][x+1+i] == arr[y][x-i]:
                        cnt += 1
                if cnt == m:
                    return ['y',x-m+1,x+m+1]
        if num % 2 == 1:
            m = num // 2
            up = y - m
            down = y + m
            right = x + m
            left = x - m
            if up >= 0 and down <= length -1:
                cnt = 0
                for i in range(1,m+1):
                    if arr[y-i][x] == arr[y+i][x]:
                        cnt += 1
                if cnt == m:
                    return ['x',y-m,y+m+1]
            if right <= length -1 and left >= 0:
                cnt = 0
                for i in range(1,m+1):
                    if arr[y][x-i] == arr[y][x+i]:
                        cnt += 1
                if cnt == m:
                    return ['y',x-m,x+m+1]
        return 0

    for i in range(N):
        for j in range(N):
            ans = Matryoshka(i,j,N,M)
            if ans != 0:
                print(f"#{tc}",end= ' ')
                if ans[0] == 'x':
                    for k in range(ans[1],ans[2]):
                        print(arr[k][j],end='')
                    print()
                elif ans[0] == 'y':
                    for k in range(ans[1],ans[2]):
                        print(arr[i][k],end='')
                    print()