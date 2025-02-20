import sys
sys.stdin = open("input.txt", "r")


T = int(input()) # 테케
for idx in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    max_l = 0 # 최장 거리
    # 델타
    d_y = [-1,1,0,0]
    d_x = [0,0,-1,1]

    for i in range(n):
        for j in range(n): # 배열을 돌면서 경로의 최댓값 찾기
            x, y = i, j
            cnt = 1


            while True: # 옮길 위치가 없을 때까지 반복

                min_n = 21e8 # 상하좌우의 값들 중의 최솟값
                min_y, min_x = -1, -1

                for i in range(4):
                    dy = y + d_y[i]
                    dx = x + d_x[i]
                    # 상하좌우가 범위를 벗어날 때, 해당 값이 상하좌우 값이 더 클때
                    if dy <0 or dx < 0 or dy >= n or dx >= n or arr[y][x] <=arr[dy][dx]:
                        continue
                    if arr[dy][dx] < min_n:
                        min_n = arr[dy][dx] # 최솟값 갱신
                        min_y, min_x = dy, dx # 최솟값의 인덱스 갱신
                
                if min_y == -1:
                    break # 이동할 곳이 없으면 중단

                x, y = min_y, min_x
                cnt += 1

            max_l = max(max_l,cnt)
    print(f'#{idx+1} {max_l}')