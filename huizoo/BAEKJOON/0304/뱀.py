import copy

N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
arr[0][0] = 2 # 뱀은 2로 표시
for _ in range(K):
    yy, xx = map(int, input().split())
    arr[xx-1][yy-1] = 1   # 1은 사과

L = int(input())
y, x = 0, 0
direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
d = 2 # 기본값 우측으로 출발
def start():
    cnt = 0
    for _ in range(L):
        game = copy.deepcopy(arr)
        X, C = map(int, input().split())
        dy, dx = direct[d]
        if d == 2 or d == 3:
            for i in range(1, X):
                cnt += 1
                nx = x+dx*i
                if nx < 0 or nx >= N: return cnt
                if arr[y][nx] == 0:
                    arr[y][x] = 2
                elif arr[y][nx] == 1:




start()