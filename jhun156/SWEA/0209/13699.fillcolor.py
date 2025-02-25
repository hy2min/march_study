# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,T+1):
    n = int(input()) # 색칠할 영역 수
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 시작인덱스, 끝인덱스, 색깔종류 총 5개 숫자
    lst = [[0] * 10 for _ in range(10)] # 10 x 10 배열

    def color(y1,x1,y2,x2,num):     # num은 색깔 종류, 1은 빨강, 2는 파랑, 3은 보라
        for i in range(y2-y1+1):
            for j in range(x2-x1+1):
                if lst[y1+i][x1+j] != num and lst[y1+i][x1+j] != 3:
                    lst[y1+i][x1+j] += num

    for i in range(n):
        color(*arr[i])

    Sum = 0
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                Sum += 1

    print(f"#{test_case} {Sum}")