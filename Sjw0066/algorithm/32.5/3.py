import copy

arr=[
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S'],
]

ret=copy.deepcopy(arr)

direct_y=[0,0,1,-1,0]
direct_x=[1,-1,0,0,0]

str1=input()

for target in str1:
    for i in range(3):
        for j in range(6):
            if arr[i][j] == target:
                for k in range(5):
                    dy=direct_y[k]+i
                    dx=direct_x[k]+j
                    if dy<0 or dx<0 or dx>5 or dy>2:continue
                    if ret[dy][dx] == '#':
                        ret[dy][dx] = arr[dy][dx]
                        continue
                    ret[dy][dx] = '#'
                continue

for i in ret:
    print(*i,sep="")


