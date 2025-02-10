import sys
sys.stdin = open('input.txt','r')

T= 10

for tc in range(1, T + 1):
    tc=int(input())
    data=[list(map(int,input().split())) for _ in range(100)]
    direct_y=[1,0,0]
    direct_x=[0,1,-1]
    start_c=0

    def search_road(start_x):
        y=0
        x=start_x
        d=0

        while y<99:
            if d==0:# 아래로 내려가는 중이면
                if x>0 and data[y][x-1]: # 왼쪽에 값이 있으면 왼쪽 가기
                    d=2
                if x<99 and data[y][x+1]:# 오른쪽에 값이 있으면 오른쪽 가기
                    d=1
            else:
                if data[y+1][x]: # 좌나 우로 가는중이면 직진
                    d=0
            y+=direct_y[d]
            x+=direct_x[d]

        if data[99][x]==2:
            return start_x

    answer=0

    for i in range(100):
        if data[0][i] == 1:
            answer = search_road(i)
            if answer == i :
                break
    print(f'#{tc} {answer}')