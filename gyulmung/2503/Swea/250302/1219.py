import sys
sys.stdin = open('input.txt', 'r')

def Find(now, visited):
    if now == 99:
        return True
    visited[now] = True
    for i in range(100):
        if arr[now][i] == 1 and not visited[i]:
            if Find(i, visited):
                return True
    return False



for test in range(1, 11):
    T, N = map(int, input().split())
    arr = [[0]*100 for _ in range(100)]
    lst = list(map(int, input().split()))
    route = []
    for i in range(0, N*2, 2):
        route.append([lst[i], lst[i+1]])
    for i in range(N):
        arr[route[i][0]][route[i][1]] = 1
    visited = [False] * 100
    result = Find(0, visited)

    if result:
        print(f'#{test} {1}')
    else:
        print(f'#{test} {0}')