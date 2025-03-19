import sys
sys.stdin = open("input.txt", "r")

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = tuple(tuple(map(int, input().split())) for _ in range(N))
    visited = [[0]*N for _ in range(N)]
    Max = N**2+1
    dat = [0]*Max
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            # 현재 숫자에서 1 증가한 숫자가 근처에 있으면 dat[숫자] = 1
            for dy, dx in d:
                ny, nx = dy+i, dx+j
                if ny<0 or nx<0 or ny>=N or nx>=N: continue
                # 1 증가한 숫자 자리는 방문배열 체크
                nxt = arr[ny][nx]
                if visited[ny][nx]: continue
                if nxt == now+1:
                    visited[ny][nx] = 1
                    dat[now] = 1

    i = 1
    start = 1
    max_room = 1
    while i < Max:
        if dat[i]:
            cnt = 2
            for j in range(i+1, Max):
                if dat[j]:
                    cnt += 1
                else:
                    break
            if max_room < cnt:
                max_room = cnt
                start = i
            i += cnt
        else:
            i += 1

    print(f'#{tc} {start} {max_room}')
