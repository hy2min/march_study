arr = [
    [3,2,5,3],
    [7,6,1,6],
    [4,9,2,7]
]

a,b,c,d = map(int,input().split())
arr2 = [a,b,c,d]

def gear(col,n) :
    global arr
    column = [arr[i][col] for i in range(3)]
    column = column[-n:] + column[:-n]
    for i in range(3):
        arr[i][col] = column[i]

for i in range(4):
    gear(i,arr2[i])


for i in range(3):
    for j in range(4):
        print(arr[i][j],end='')
    print()