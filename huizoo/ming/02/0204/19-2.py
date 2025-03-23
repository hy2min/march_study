map1 = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2],
]

dy = [-1,-1,1,1]
dx = [-1,1,-1,1]

def sum1(y, x) :    
    total = 0
    for i in range(4) : 
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5 : 
            total += map1[ny][nx]
    return total

max_sum = -float('inf')
max_coords = []
for i in range(5) : 
    for j in range(5) : 
        current_sum = sum1(i, j)
        if current_sum > max_sum : 
            max_sum = current_sum
            max_coords = [(i, j)]
        elif current_sum == max_sum :  
            max_coords.append((i, j))
            
print(' '.join(map(str, *max_coords)))