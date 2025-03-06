bingo = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]
flag = 0
n = 0
def BingBing(arr): 
    cnt = 0
    for row in arr : 
        if row.count(0) == 5 : 
            cnt += 1
    
    for row in list(zip(*arr)) :
        if row.count(0) == 5 : 
            cnt += 1
    temp1 = 0
    temp2 = 0
    for i in range(5) : 
        if arr[i][-i-1] == 0 : 
            temp1 += 1
        if arr[i][i] == 0 : 
            temp2 += 1
    if temp1 == 5 : 
        cnt += 1
    if temp2 == 5 : 
        cnt += 1
    
    if cnt >= 3 : 
        return 1
    return 0

for y in range(5) : 
    for x in range(5) :
        n += 1
        for i in range(5) :
            for j in range(5) : 
                if bingo[i][j] == answer[y][x] : 
                    bingo[i][j] = 0
                    flag = BingBing(bingo)
                    if flag : 
                        break
            if flag : 
                break
        if flag : 
            break
    if flag : 
        break
if flag : 
    print(n)