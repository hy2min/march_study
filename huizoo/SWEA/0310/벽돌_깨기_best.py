# 보완 (훈수)
T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def shoot(level, remains, now_arr):
    global min_blocks  # 함수 내부에서 수정이 필요할 경우에만 global를 사용

    # 구슬 모두 사용 했을 때, 더이상 깨질 벽돌 없을 때 결과 업데이트 후 종료
    if level == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    flag = False
    # 구슬 떨어 뜨릴 열 선택
    for col in range(W):
        copy_arr = [row[:] for row in now_arr]
        row = -1
        for r in range(H):
            flag = False
            if copy_arr[r][col]:
                nn = 0
                # 구슬이 떨어질 벽돌의 깊이(N-level)에 따른 유효값(1초과) 탐색 ( 가지치기 )
                while nn <= N - level and r + nn < H:
                    if copy_arr[r + nn][col] > 1:
                        flag = True  # 유효 벽돌  유무
                        row = r
                        break
                    nn += 1
            if flag:
                break

        if row == -1:
            continue

        # 현재 깨질 벽돌 리스트
        li = [(row, col, copy_arr[row][col])]
        now_remains = remains - 1
        copy_arr[row][col] = 0  # 첫번째 벽돌 제거

        while li:
            r, c, p = li.pop()

            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:  # 범위 확인
                        continue
                    if copy_arr[nr][nc] == 0:  # 벽돌이 없다면 패스
                        continue
                    li.append((nr, nc, copy_arr[nr][nc]))  # 새로운 벽돌 추가
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        for c in range(W):
            idx = H - 1
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1
        shoot(level + 1, now_remains, copy_arr)
    if flag == False:
        remains -= N - level
        if remains < 0:
            remains = 0
        min_blocks = min(min_blocks, remains)
        return


for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0
    for row in arr:
        for el in row:
            if el:
                blocks += 1
    shoot(0, blocks, arr)
    print(f'#{tc} {min_blocks}')