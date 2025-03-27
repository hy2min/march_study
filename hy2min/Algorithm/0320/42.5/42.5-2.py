dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(level, temp_arr, total_count):
    global max_count, ans

    if level == n:
        if max_count < total_count:
            max_count = total_count
            ans = current_ch[:]
        return

    for i in range(len(ch_list)):
        if visited[i]:
            continue

        y, x, ch = ch_list[i]
        visited[i] = 1

        new_arr = [row[:] for row in temp_arr]
        cnt = 0

        if new_arr[y][x].isalpha():
            new_arr[y][x] = '_'
            cnt += 1


        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx <0 or ny >= 4 or nx >= 4 or new_arr[ny][nx] == '_':
                continue
            new_arr[ny][nx] = '_'
            cnt += 1

        current_ch.append(ch)
        dfs(level+1, new_arr, total_count+cnt)
        current_ch.pop()
        visited[i] = 0
arr = [list(input()) for _ in range(4)]
n = int(input())

ch_list = []
for i in range(4):
    for j in range(4):
        if arr[i][j].isalpha():
            ch_list.append([i, j, arr[i][j]])

ch_list.sort(key=lambda x: ord(x[2]))
temp_arr = [row[:] for row in arr]

visited = [0] * len(ch_list)

max_count = -21e8
current_ch = []
ans = []

dfs(0, temp_arr,0)
ans.sort(key=lambda x: ord(x))
print(" ".join(ans))