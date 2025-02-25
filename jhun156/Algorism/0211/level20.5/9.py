arr = [
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2],
]

n,m = map(int,input().split())

def find_max(y,x):
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += arr[y+i][x+j]
    return sum

Max = 0
Y,X = 0,0
for i in range(4-n+1):
    for j in range(5-m+1):
        ans = find_max(i,j)
        if Max < ans:
            Max = ans
            Y,X = i,j
print(f"({Y},{X})")