N = int(input())
# 좌표의 범위가 0~1000 이므로, 전체 영역을 나타내는 배열 생성
road = [0] * 1001  

# 각 기둥 정보를 road 배열에 반영
min_x, max_x = 1001, 0
for _ in range(N):
    x, h = map(int, input().split())
    road[x] = h
    min_x = min(min_x, x)
    max_x = max(max_x, x)

# 전체 영역에서 실제 기둥이 있는 최소~최대 좌표 범위만 고려
road = road[min_x:max_x+1]

# 최고 높이와 그 인덱스를 찾기
max_height = max(road)
max_index = road.index(max_height)

area = 0
# 왼쪽 영역: 왼쪽부터 최고 높이 기둥까지
current = 0
for h in road[:max_index]:
    if h > current:
        current = h
    area += current

# 오른쪽 영역: 오른쪽부터 최고 높이 기둥까지 (역방향으로 계산)
current = 0
for h in road[:max_index:-1]:  # road[max_index+1:]를 뒤집어 순회
    if h > current:
        current = h
    area += current

# 최고 높이 기둥의 면적 (최고 높이 기둥이 여러 개라면, 이 부분은 최고 기둥이 차지하는 너비로 자동 계산됨)
area += max_height

print(area)
