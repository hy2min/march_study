arr = [
    ['_','_','_'],
    ['_','_','_'],
    ['A','T','K'],
    ['_','_','_'],
    ['_','_','_'],
]

a = [2, 0]
t = [2, 1]
k = [2, 2]
for _ in range(7) : 
    pick, order = input().split()
    if order == 'UP' : 
        if pick == 'A' : 
            if arr[a[0]-1][a[1]] == 'T' : 
                t[0] += 1
            elif arr[a[0]-1][a[1]] == 'K' : 
                k[0] += 1
            arr[a[0]][a[1]], arr[a[0]-1][a[1]] = arr[a[0]-1][a[1]], arr[a[0]][a[1]]
            a[0] -= 1
        elif pick == 'T' : 
            if arr[t[0]-1][t[1]] == 'A' : 
                a[0] += 1
            elif arr[t[0]-1][t[1]] == 'K' : 
                k[0] += 1
            arr[t[0]][t[1]], arr[t[0]-1][t[1]] = arr[t[0]-1][t[1]], arr[t[0]][t[1]]
            t[0] -= 1
        elif pick == 'K' : 
            if arr[k[0]-1][k[1]] == 'T' : 
                t[0] += 1
            elif arr[k[0]-1][k[1]] == 'A' : 
                a[0] += 1
            arr[k[0]][k[1]], arr[k[0]-1][k[1]] = arr[k[0]-1][k[1]], arr[k[0]][k[1]]
            k[0] -= 1

    elif order == 'DOWN' : 
        if pick == 'A' : 
            if arr[a[0]+1][a[1]] == 'T' : 
                t[0] -= 1
            elif arr[a[0]+1][a[1]] == 'K' : 
                k[0] -= 1
            arr[a[0]][a[1]], arr[a[0]+1][a[1]] = arr[a[0]+1][a[1]], arr[a[0]][a[1]]
            a[0] += 1
        elif pick == 'T' :
            if arr[t[0]+1][t[1]] == 'A' : 
                a[0] -= 1
            elif arr[t[0]+1][t[1]] == 'K' : 
                k[0] -= 1
            arr[t[0]][t[1]], arr[t[0]+1][t[1]] = arr[t[0]+1][t[1]], arr[t[0]][t[1]]
            t[0] += 1
        elif pick == 'K' :
            if arr[k[0]+1][k[1]] == 'T' : 
                t[0] -= 1
            elif arr[k[0]+1][k[1]] == 'A' : 
                a[0] -= 1
            arr[k[0]][k[1]], arr[k[0]+1][k[1]] = arr[k[0]+1][k[1]], arr[k[0]][k[1]]
            k[0] += 1

    elif order == 'LEFT' : 
        if pick == 'A' :
            if arr[a[0]][a[1]-1] == 'T' : 
                t[1] += 1
            elif arr[a[0]][a[1]-1] == 'K' : 
                k[1] += 1
            arr[a[0]][a[1]], arr[a[0]][a[1]-1] = arr[a[0]][a[1]-1], arr[a[0]][a[1]]
            a[1] -= 1
        elif pick == 'T' :
            if arr[t[0]][t[1]-1] == 'A' : 
                a[1] += 1
            elif arr[t[0]][t[1]-1] == 'K' : 
                k[1] += 1
            arr[t[0]][t[1]], arr[t[0]][t[1]-1] = arr[t[0]][t[1]-1], arr[t[0]][t[1]]
            t[1] -= 1
        elif pick == 'K' :
            if arr[k[0]][k[1]-1] == 'A' : 
                a[1] += 1
            elif arr[k[0]][k[1]-1] == 'T' : 
                t[1] += 1
            arr[k[0]][k[1]], arr[k[0]][k[1]-1] = arr[k[0]][k[1]-1], arr[k[0]][k[1]]
            k[1] -= 1

    elif order == 'RIGHT' : 
        if pick == 'A' : 
            if arr[a[0]][a[1]+1] == 'T' : 
                t[1] -= 1
            elif arr[a[0]][a[1]+1] == 'K' : 
                k[1] -= 1
            arr[a[0]][a[1]], arr[a[0]][a[1]+1] = arr[a[0]][a[1]+1], arr[a[0]][a[1]]
            a[1] += 1
        elif pick == 'T' : 
            if arr[t[0]][t[1]+1] == 'A' : 
                a[1] -= 1
            elif arr[t[0]][t[1]+1] == 'K' : 
                k[1] -= 1
            arr[t[0]][t[1]], arr[t[0]][t[1]+1] = arr[t[0]][t[1]+1], arr[t[0]][t[1]]
            t[1] += 1
        elif pick == 'K' :
            if arr[k[0]][k[1]+1] == 'T' : 
                t[1] -= 1
            elif arr[k[0]][k[1]+1] == 'A' : 
                a[1] -= 1
            arr[k[0]][k[1]], arr[k[0]][k[1]+1] = arr[k[0]][k[1]+1], arr[k[0]][k[1]]
            k[1] += 1

print('\n'.join(''.join(row) for row in arr))