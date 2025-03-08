arr = [['G', 'K', 'T'],
       ['P', 'A', 'C'],
       ]

a, b = input().split()

def isExist(x, y) : 
    cnt = 0
    for row in arr : 
        if x in row : 
            cnt += 1
        if y in row : 
            cnt += 1
    if cnt == 2 : 
        return '대발견'
    elif cnt == 1 : 
        return '중발견'
    else : 
        return '미발견'

ret = isExist(a, b)
print(ret)