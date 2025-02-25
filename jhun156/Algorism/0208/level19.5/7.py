lst = [
    [3,5,1],
    [3,8,1],
    [1,1,5],
]

bitarray = [[i for i in map(int,input().split())] for _ in range(2)]

def get_sum(y,x):
    Sum = 0
    for i in range(2):
        for j in range(2):
            if bitarray[i][j] == 1:
                Sum += lst[y+i][x+j]
    return Sum

Max,Y,X = 0,0,0
for i in range(2):
    for j in range(2):
        ans = get_sum(i,j)
        if Max < ans:
            Max = ans
            Y,X = i,j

print(f"({Y},{X})")
