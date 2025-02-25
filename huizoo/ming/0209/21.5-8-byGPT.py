arr = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['A', 'T', 'K'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

# 캐릭터 위치 관리
positions = {'A': [2, 0], 'T': [2, 1], 'K': [2, 2]}

# 방향 정의
directions = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}

for _ in range(7):  # 명령 7번 처리
    pick, order = input().split()
    dx, dy = directions[order]
    x, y = positions[pick]
    nx, ny = x + dx, y + dy

    # 이동 가능하면 처리
    if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
        if arr[nx][ny] in positions:  # 충돌 시 위치 교환
            other = arr[nx][ny]
            positions[other] = [x, y]
        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
        positions[pick] = [nx, ny]  # 선택된 캐릭터 새 위치 저장

# 결과 출력
print('\n'.join(''.join(row) for row in arr))
