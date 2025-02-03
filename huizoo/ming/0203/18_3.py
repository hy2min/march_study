arr = [[1,3,3,5,1],
       [3,6,2,4,2],
       [1,9,2,6,5],
       ]

N = int(input())

dat = [0]*10

for row in arr : 
    for num in row : 
        dat[num] += 1

indices = [i for i, value in enumerate(dat) if value == N]

print(*indices)