# 프로듀스 101배수
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
operations = ['*', '+', '-']
path = []
def dfs(x, num):
    if x == N:
        if num == 0:
            return
        elif num % 101 == 0:
            print(''.join(map(str, path)))
        return

    now = arr[x]

    if x == 0:
        num += now
    else:
        now_op = path[-1]
        if now_op == '*':
            num *= now
        elif now_op == '+':
            num += now
        elif now_op == '-':
            num -= now

    path.append(now)
    if x < N-1:
        for operation in operations:
            path.append(operation)
            dfs(x+1, num)
            path.pop()
    else:
        dfs(x+1, num)

    path.pop()


dfs(0, 0)