arr=[3,7,4,1,2,6]
univer=[]
for i in range(2):
    univer.append(list(map(int,input().split())))

def isExist(a):
    if a in arr:
        return 'OK'
    else:
        return 'NO'
for i in univer:
    ret=[]
    for j in i:
        ret.append(isExist(j))
    print(*ret)