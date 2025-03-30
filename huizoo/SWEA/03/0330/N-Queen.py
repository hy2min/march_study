import sys
sys.stdin = open("input.txt", "r")

def abc(x):
    global cnt
    if x >= n:
        cnt += 1
        return

    for i in range(n):
        if visited[i] == 1 or visited2[i+x] == 1 or visited3[i-x+n] == 1: continue
        visited[i] = 1
        visited2[i+x] = 1
        visited3[i-x+n] = 1
        abc(x+1)
        visited[i] = 0
        visited2[i+x] = 0
        visited3[i-x+n] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    visited = [0]*n
    visited2 = [0]*(2*n)
    visited3 = [0]*(2*n)
    cnt = 0
    abc(0)
    print(f'#{tc} {cnt}')