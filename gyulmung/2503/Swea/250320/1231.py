import sys
sys.stdin = open('input.txt','r')

def in_order(now):
    if now > len(lst) - 1 or visited[now] == 1:
        return

    in_order(now*2)
    ret.append(lst[now])
    visited[now] = 1
    in_order(now*2+1)

T = 10

for test in range(1, T+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input().split()))
    lst = [0]
    for i in arr:
        lst.append(i[1])
    visited = [0]*(n+1)
    ret = []
    in_order(1)
    ret = "".join(ret)
    print(f'#{test} {ret}')
