image = []
for i in range(4):
    row = []
    row.extend(list(map(int,input().split())))
    image.append(row)

def rectSum(y,x):
    Sum = 0
    for i in range(2):
        for j in range(3):
            Sum += image[y+i][x+j]
    return Sum
Max = 0
Y,X = 0,0
for i in range(3):
    for j in range(2):
        ans = rectSum(i,j)
        if Max < ans:
            Max = ans
            Y,X = i,j
print(f"({Y},{X})")
