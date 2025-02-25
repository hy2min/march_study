arr = list(map(int, input().split()))
n = int(input())
Max = 0


def dfs(turn, total):
    global arr, Max
    if turn == n:
        Max = max(Max, total)
        return
    # 턴 시작 시 현재 상태 백업 후, 한 번만 doubling 적용
    backup = arr[:]
    if turn > 0:
        for i in range(6):
            arr[i] *= 2

    ranges = [(0, 2), (3, 6), (1, 5)]

    # 한 턴에서 3마리 독수리 선택 (내부 DFS)
    def dfs_eagle(eagle, local_sum):
        if eagle == 3:
            dfs(turn + 1, total + local_sum)
            return
        st, ed = ranges[eagle]
        state_backup = arr[:]  # 각 분기마다 현재 상태 백업
        for j in range(st, ed):
            if arr[j] != 0:
                ate = arr[j]
                arr[j] = 0
                dfs_eagle(eagle + 1, local_sum + ate)
                arr[:] = state_backup[:]  # 백트래킹

    dfs_eagle(0, 0)
    arr[:] = backup[:]  # 이번 턴 끝나고 상태 복원


dfs(0, 0)
print(Max)
