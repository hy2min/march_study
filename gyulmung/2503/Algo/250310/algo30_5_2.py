import sys
sys.stdin = open('input.txt', 'r')

# 승부차기 인원
N = int(input())

# 외부에 저장
path = [0]*N
visited = [0]*2
arr = ['o', 'x']

# 함수
def goal(level):
    global path
    if level == N:
        print(*path, sep = '')
        return

    for i in range(2):
        path[level]=(arr[i])
        visited[i] = 1
        goal(level+1)
        visited[i] = 0
#출력
visited[0] = 1
goal(0)
