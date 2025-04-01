arr = [ ['P', 'O', 'T', 'I', 'O'],
        ['A', 'B', 'C', 'D', 'E'],
        ['Y', 'O', 'U', 'R', 'E']]

a, b = map(int, input().split())

for i in range(3):
    for j in range(a, b + 1):
        print(arr[i][j],end = '')