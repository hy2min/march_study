arr = [
    ['_','_','_'],
    ['_','_','_'],
    ['A','T','K'],
    ['_','_','_'],
    ['_','_','_'],
]
a, t, k = [2, 0], [2, 1], [2, 2]
for _ in range(7):
    alp, order = input().split()
    if alp == 'A':
        if order == 'UP':
            arr[a[0]][a[1]], arr[a[0] - 1][a[1]] = arr[a[0] - 1][a[1]], arr[a[0]][a[1]]
            a[0] -= 1
        elif order == 'DOWN':
            arr[a[0]][a[1]], arr[a[0] + 1][a[1]] = arr[a[0] + 1][a[1]], arr[a[0]][a[1]]
            a[0] += 1
        elif order == 'LEFT':
            arr[a[0]][a[1]], arr[a[0]][a[1] - 1] = arr[a[0]][a[1] - 1], arr[a[0]][a[1]]
            a[1] -= 1
        elif order == 'RIGHT':
            arr[a[0]][a[1]], arr[a[0]][a[1] + 1] = arr[a[0]][a[1] + 1], arr[a[0]][a[1]]
            a[1] += 1
    elif alp == 'T':
        if order == 'UP':
            arr[t[0]][t[1]], arr[t[0] - 1][t[1]] = arr[t[0] - 1][t[1]], arr[t[0]][t[1]]
            t[0] -= 1
        elif order == 'DOWN':
            arr[t[0]][t[1]], arr[t[0] + 1][t[1]] = arr[t[0] + 1][t[1]], arr[t[0]][t[1]]
            t[0] += 1
        elif order == 'LEFT':
            arr[t[0]][t[1]], arr[t[0]][t[1] - 1] = arr[t[0]][t[1] - 1], arr[t[0]][t[1]]
            t[1] -= 1
        elif order == 'RIGHT':
            arr[t[0]][t[1]], arr[t[0]][t[1] + 1] = arr[t[0]][t[1] + 1], arr[t[0]][t[1]]
            t[1] += 1
    else:
        if order == 'UP':
            arr[k[0]][k[1]], arr[k[0] - 1][k[1]] = arr[k[0] - 1][k[1]], arr[k[0]][k[1]]
            k[0] -= 1
        elif order == 'DOWN':
            arr[k[0]][k[1]], arr[k[0] + 1][k[1]] = arr[k[0] + 1][k[1]], arr[k[0]][k[1]]
            k[0] += 1
        elif order == 'LEFT':
            arr[k[0]][k[1]], arr[k[0]][k[1] - 1] = arr[k[0]][k[1] - 1], arr[k[0]][k[1]]
            k[1] -= 1
        elif order == 'RIGHT':
            arr[k[0]][k[1]], arr[k[0]][k[1] + 1] = arr[k[0]][k[1] + 1], arr[k[0]][k[1]]
            k[1] += 1

print('\n'.join(''.join(row) for row in arr))