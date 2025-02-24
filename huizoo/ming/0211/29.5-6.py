time = list(map(int, input().split()))
wheel = [
    [3, 2, 5, 3],
    [7, 6, 1, 6],
    [4, 9, 2, 7],
]

for i in range(4):
    for _ in range(time[i]):       
        wheel[0][i], wheel[1][i], wheel[2][i] = wheel[2][i], wheel[0][i], wheel[1][i]
    
print('\n'.join(''.join(map(str, row))for row in wheel))