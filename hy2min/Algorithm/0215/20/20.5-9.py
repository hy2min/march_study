def find_sum(n,m):
    size_sum = 0
    for y in range(n):
        for x in range(m):
            size_sum += arr[i+y][j+x]
    return size_sum
arr = [
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2],
]

n, m = map(int, input().split())
max_sum = -21e8
y_max, x_max = -1, -1
for i in range(4-n+1):
    for j in range(5-m+1):
        if max_sum < find_sum(n,m):
            max_sum = find_sum(n,m)
            y_max, x_max = i,j

print(f'({y_max},{x_max})')
