# import sys
# sys.stdin = open("input.txt","r")

N,K=map(int,input().split())
# N = 학생수, K = 방에 있을 수 있는 최대 학생 수
# 남학생 1, 여학생 0
# 두번째 인자는 학년
lst = [[0] * 6 for _ in range(2)]
for i in range(N):
    s,n = map(int,input().split())
    lst[s][n-1] += 1
ans = 0
    # lst[0] = 여학생
    # lst[1] = 남학생 lst[s][n-1] = n학년 학생 수
for i in range(2):
    for j in range(6):
        if lst[i][j] == 0:
            continue
        elif lst[i][j] % K == 0:
            ans += lst[i][j] // K
        else:
            ans += (lst[i][j] // K + 1)
print(ans)

