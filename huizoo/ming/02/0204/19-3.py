arr = [
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
]

yx = [list(map(int, input().split())) for _ in range(2)]

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]


for i in range(2) :     
    for j in range(8) : 
        ny, nx = yx[i][0]+dy[j], yx[i][1]+dx[j]
        if 0 <= ny < 4 and 0 <= nx < 5 : 
            arr[ny][nx] = '#'

print('\n'.join(' '.join(row)for row in arr))