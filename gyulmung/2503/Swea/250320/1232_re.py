import sys
sys.stdin = open('input.txt', 'r')


from collections import deque

def dfs(now):
    if len(arr[now]) > 2:
        a, left, right = arr[now][1:]
        dfs(int(left))
        dfs(int(right))
        total.append(a)
    else:
        a = arr[now][1]
        total.append(a)


T = 10
for test in range(1, T+1):
    n = int(input())
    arr = [[0, 0]]
    for i in range(n):
        arr.append(list(input().split()))
    total = deque()
    ret = []
    hide = []

    dfs(1)

    for i in total:
        if i.isdigit():
            ret.append(int(i))
        else:
            a = ret.pop()
            b = ret.pop()
            if i == '+':
                ret.append(b+a)
            elif i == '-':
                ret.append(b-a)
            elif i == '*':
                ret.append(b*a)
            elif i == '/':
                ret.append(b//a)
    print(f'#{test}', *ret)

