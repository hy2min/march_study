
def find_boss(n):
    if node[n] == '-':
        return n
    ret = find_boss(node[n])
    node[n] = ret
    return ret

def union(y,x):
    boss_y, boss_x = find_boss(y), find_boss(x)
    if boss_y == boss_x:
        return 0
    node[boss_x] = boss_y
    return 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
node = ['-'] * n

flag = 0
for i in range(n):
    for j in range(i, n):
        if arr[i][j] == 1:
            ret = union(i,j)
            if not ret:
                flag = 1
                break
    if flag:
        break
if flag:
    print('cycle 발견')
else:
    print('미발견')