from collections import deque

def bhc(y, x):
    q = deque([(y, x)])
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    cnt = 1
    while q:
        yy, xx = q.popleft()
        if visited[yy][xx] >= L: continue  # 시간 초과시 이동 X
        pipe = arr[yy][xx]
        for dy, dx in d[pipe]:
            ny, nx = yy + dy, xx + dx
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue  # 인덱스 초과 방지
            if arr[ny][nx] not in pos[(dy, dx)]: continue  # 파이프 호환 확인(0도 자연스레 걸러짐)
            if visited[ny][nx]: continue  # 방문 확인
            visited[ny][nx] = visited[yy][xx] + 1
            cnt += 1
            # if visited[ny][nx] >= L: continue  # 시간 초과시 큐에 삽입 X
            q.append((ny, nx))
    return cnt

t = int(input())
for tc in range(1, t+1):
    # N : 세로, M : 가로, R : 맨홀뚜껑 세로위치, C : 맨홀뚜껑 가로위치, L : 탈출 후 소요 시간
    N, M, R, C, L = map(int, input().split())
    # N * M 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # d는 파이프 모양 딕셔너리
    d = {
        1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, 1), (0, -1)],
        4: [(-1, 0), (0, 1)],
        5: [(0, 1), (1, 0)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)],
    }
    # 파이프 호환 여부
    pos = {
        (-1, 0): [1, 2, 5, 6],
        (1, 0): [1, 2, 4, 7],
        (0, -1): [1, 3, 4, 5],
        (0, 1): [1, 3, 6, 7],
    }

    print(f'#{tc} {bhc(R, C)}')