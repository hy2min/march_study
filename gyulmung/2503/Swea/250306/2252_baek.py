import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = map(int, input().split())

# 인접행렬 만들기
arr = [[0]*N for _ in range(N)]
for i in range(M):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1

# 학생 만들기
stu = []
for i in range(1, N+1):
    stu.append(i)

# 입력 개수 구하기
acc = [0]*N
used = [0]*N
for j in range(N):
    for i in range(N):
        if arr[i][j] == 1:
            acc[j] += 1

# 앞사람 없이 키 세우기
q = deque()
for i in range(N):
    if acc[i] == 0:
        q.append(i)
        used[i] = 1

# BFS를 돌리면서 키 정렬하기
while q:
    now = q.popleft()
    print(stu[now], end = ' ')
    for i in range(N):
        if arr[now][i] == 1 and used[i] == 0:
            if acc[i] == 1:
                acc[i] = 0
                used[i] = 1
                q.append(i)
            else:
                acc[i] -= 1


# GPT 코드

from collections import deque

N, M = map(int, input().split())

# 인접 리스트 사용
arr = [[] for _ in range(N)]
edges = set()

for _ in range(M):
    y, x = map(int, input().split())
    if (y, x) not in edges:  # 중복 방지
        edges.add((y, x))
        arr[y-1].append(x-1)

# 진입 차수 계산
acc = [0] * N
for i in range(N):
    for j in arr[i]:
        acc[j] += 1

# 큐 초기화 (deque 사용)
q = deque()
used = bytearray(N)  # 메모리 최적화

for i in range(N):
    if acc[i] == 0:
        q.append(i)
        used[i] = 1

# BFS 실행 (O(N + M))
while q:
    now = q.popleft()
    print(now + 1, end=' ')  # 학생 번호 출력

    for nxt in arr[now]:
        if used[nxt] == 0:
            acc[nxt] -= 1
            if acc[nxt] == 0:
                used[nxt] = 1
                q.append(nxt)