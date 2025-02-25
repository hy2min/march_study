arr = [
    [3, 5, 9],
    [4, 2, 1],
    [5, 1, 5],
]

inputs = list(map(int,input().split()))

def isExist():
    for i in inputs:
        for row in arr:
            if i in row:
                print(f'{i}:존재')
                break
        else:    
            print(f'{i}:미발견')
       
isExist()