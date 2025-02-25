N = int(input())
near_matrix = [list(map(int,input().split())) for _ in range(N)]

# 음. 요즘 dfs,bfs만 많이 풀어서 머리가 재귀에 멍해졌는데
# 이 문제는 꼭 재귀할필요없이 간단히 풀릴방법이 보여서 이렇게 풀었습니다.
boss = []
under = []
for i in range(N):
    if near_matrix[i][0] == 1:
        boss.append(i)

for i in range(N):
    if near_matrix[0][i] == 1:
        under.append(i)

print("boss:",end='')
print(*boss)
print("under:",end='')
print(*under)