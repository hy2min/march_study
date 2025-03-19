import sys
sys.stdin = open("input.txt", "r")

def find_boss(x):
    if student[x] != x:
        student[x] = find_boss(student[x])
    return student[x]

def union(a, b):
    global cnt
    a_boss, b_boss = find_boss(a), find_boss(b)
    if a_boss == b_boss:
        return
    if rank[a_boss] > rank[b_boss]:
        student[b_boss] = a_boss
    else:
        student[a_boss] = b_boss
        if rank[a_boss] == rank[b_boss]:
            rank[b_boss] += 1
    cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    student = [i for i in range(N+1)]
    rank = [1]*(N+1)
    cnt = 0
    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    print(f'#{tc} {N-cnt}')