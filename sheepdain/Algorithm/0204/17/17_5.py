arr=[3,5,9],[4,2,1],[5,1,5]
n=list(map(int,input().split()))
def isExist(a):
    for i in arr:
        for j in i:
            if a==j:
                return print(f'{a}:존재')
    return print(f'{a}:미발견')
for i in n:
    isExist(i)