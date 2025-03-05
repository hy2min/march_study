from collections import deque


def bfs(maze, n) :
    start = None
    end = None

    for i in range(n):
        for  j in  range(n) : # 행렬 반복하면서
            if maze[i][j] == 2 : #시작점
                start =  (i,j)
            elif maze[i][j] == 3: #도착점 특정
                end = (i,j)

    # 현재 위치 기준으로 상하좌우 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 초기화

    queue = deque([(start[0],start[1],-1)]) # 큐에 출발지 좌표를 추가
    visited = [[False] * n for _ in range(n)]

    # 방문 여부 확인용 visited 배열 생성
    visited[start[0]][start[1]] = True

    while queue :
        x, y, steps = queue.popleft()

        # 도착지 발견 시 지나온 칸 수 반환
        if (x,y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 이동 가능 시 큐에 추가하고 방문 처리
            if 0 <= nx < n and 0 <=  ny < n and maze[nx][ny] !=1 and not  visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny, steps +1))
    # 미도착 시 0 출력
    return 0





t = int(input())

for tc in range(1,1+t) :
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    answer = bfs(maze,N)

    print(f"#{tc} {answer}")