pattern = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
    (0,1)
]
mmap = [list(input()) for _ in range(4)]

def dfs(i, j, char):
    for dx, dy in pattern:
        new_i, new_j = i+dx, j+dy
        if new_i < 0 or new_j < 0 or new_i >= 4 or new_j >= 3 or mmap[new_i][new_j] == '#':
            continue
        mmap[new_i][new_j] = char
        mmap[i][j] = '_'


def moving(char):
    for i in range(4):
        for j in range(3):
            if mmap[i][j] == char:
                dfs(i, j ,char)
    return

for x in ['A','B','C','D']:
    moving(x)

for row in mmap:
    print("".join(row))
