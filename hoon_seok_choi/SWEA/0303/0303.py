t = int(input())
for tc in range(1, 1+t) :
    n,m = map(int,input().split())
    stone = list(map(int,input().split()))
    for _ in range(m) :
        i,j = map(int,input().split())
        i -= 1

        left = i - 1
        right = i + 1

        for _ in range(j) :
            if 0 <= left and right <n and stone[left] == stone[right] :
                stone[left] = 1 - stone[left]
                stone[right] = 1 - stone[right]

            left -= 1
            right += 1

    print(f'#{tc}', *stones)


    def dfs(y, x): dfs 함수는 좌표값을 받아서 실행되는데
        global visit, result 전역변수로 방무여부와 결과를 사용하고
        if arr[y][x] == '3': 만약 받은 좌표의 값이 3이라면
            result = 1 1울 리턴해줌
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ny = dy + y
            nx = dx + x 4방위를 돌면서
            if 0 <= nx < N and 0 <= ny < N: 만약 범위내의 값이
                if arr[ny][nx] != '1' and visit[ny][nx] == 0: 벽이 아니고 방문하지 않았다면
                    visit[ny][nx] = 1 방문여부를 체크하고
                    dfs(ny, nx)         다시 dfs를 돌림 = 3을 찾을때 까지


    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        result = 0
        visit = [[0] * N for i in range(N)]
        arr = [list(input()) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] == '2': 받은 리스트를 돌며 시작점을 찾아내고
                    dfs(i, j) 그 시작점을 dfs 함수에 던짐
        print(f"#{t} {result}")
