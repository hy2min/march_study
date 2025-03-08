arr = [
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2],
]
n, m = map(int, input().split())
Max = 0
y, x = 0, 0
for i in range(5-n):
    for j in range(6-m):
        Sum = 0
        for k in range(n):
            for l in range(m):
               Sum += arr[i+k][j+l]
        if Max < Sum:
            Max = Sum
            y, x = i, j

print(f'({y},{x})')