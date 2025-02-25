arr = [
    [3,5,9],
    [4,2,1],
    [5,1,5],
]

lst = [i for i in map(int,input().split())]

def isExist(a):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == a:
                return 1
    else:
        return 0
            
for num in lst:
    a = isExist(num)
    if a == 1:
        print(f"{num}:존재")
    else:
        print(f"{num}:미발견")
