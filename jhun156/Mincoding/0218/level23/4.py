singer = ['B','T','S','K','R']
n = int(input())
path = [0] * n
used = [0] * 5
cnt = 0

def select(num):
    global cnt
    if num == n:
        if 'S' in path:
            cnt += 1
        return

    for i in range(5):
        if used[i] == 1:
            continue
        path[num] = singer[i]
        used[i] = 1
        select(num+1)
        used[i] = 0

select(0)
print(cnt)