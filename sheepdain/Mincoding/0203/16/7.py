arr=[]
for i in range(3):
    arr.append(input())
def FIND(arr):
    for i in arr:
        for j in i:
            if j=='M':
                return print('M이 존재합니다')
    return print('M이 존재하지 않습니다')
FIND(arr)