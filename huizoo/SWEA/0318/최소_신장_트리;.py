import sys

sys.stdin = open("input.txt", "r")

def find_boss(x):
    if parent[x] != x:
        parent[x] = find_boss(parent[x])
    return parent[x]

def union(a, b, i):
    global cnt, total
    a_boss, b_boss = find_boss(a), find_boss(b)
    if a_boss == b_boss:
        return
    total += arr[i][2]
    cnt += 1
    parent[b_boss] = a_boss


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda x: x[2])
    parent = [i for i in range(V+1)]
    total = 0
    cnt = 0
    for i in range(E):
        if cnt == V-1:
            print(total)
            break
        union(arr[i][0], arr[i][1], i)

