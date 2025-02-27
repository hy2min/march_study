apt = [
    [15, 18, 17],
    [4, 6, 9],
    [10, 1, 3],
    [7, 8, 9], 
    [15, 2, 6]
]

familly=list(map(int,input().split()))

def isPattern(y):
    if apt[y] == familly:
        return 1
    else:
        return 0
flag=0
floor=0

for i in range(5):
    flag=isPattern(i)
    floor=5-i
    
    if flag==1:
        print(f'{floor}층')
        break


    
