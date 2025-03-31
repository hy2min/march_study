def rectSum(y, x) : 
    dy = [0, 0, 0, 1, 1, 1]
    dx = [0, 1, 2, 0, 1, 2]    
    total = 0
    for i in range(6) : 
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4 : 
            total += image[ny][nx]
    return total

image = [list(map(int, input().split())) for _ in range(4)]

max_total = -float('inf')
current_max = []
for i in range(4) : 
    for j in range(4) : 
        ret = rectSum(i, j)
        if  ret > max_total : 
            max_total = ret
            current_max = [(i, j)]
        elif ret == max_total : 
            current_max.append((i, j))

print(' '.join(f'({y},{x})' for y, x in current_max))