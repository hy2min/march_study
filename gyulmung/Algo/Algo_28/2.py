N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(N, arr):
    boss = -1
    member= []

    for i in range(N):
        if arr[i][0] == 1:
            boss = i
            break

    for i in range(N):
        if arr[0][i] == 1:
            member.append(i)

    return boss, member

boss, members = dfs(N, arr)
print(f'boss:{boss}')
print(f"under:{' '.join(map(str, members))}")
