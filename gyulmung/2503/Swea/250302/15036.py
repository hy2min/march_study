import sys
sys.stdin = open('input.txt', 'r')

def Find(now, V, goal, visited):
    if now == goal - 1:
        return True
    visited[now] = True
    for i in range(V):
        if arr[now][i] == 1  and not visited[i]:
            if Find(i, V, goal, visited):
                return True
    return False

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*V for _ in range(V)]
    result = 0
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start-1][end-1] = 1

    starting, goal = map(int, input().split())

    visited = [False] * V
    result = Find(starting - 1, V, goal, visited)

    if result:
        print(f'#{test} {1}')
    else:
        print(f'#{test} {0}')