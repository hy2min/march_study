def bingo_check(arr):
    cnt = 0
    
    for row in arr:
        if row.count(0) == 5:
            cnt += 1
    
    for column in list(zip(*arr)):
        if column.count(0) == 5:
            cnt += 1
    
    if all(arr[i][i] == 0 for _ in range(5)):
        cnt += 1
    if all(arr[i][4-i] == 0 for _ in range(5)):
        cnt += 1
    if cnt >=3 :
        return 1

arr = [list(map(int,input().split())) for _ in range(5)]
mc = [int(n) for _ in range(5) for n in input().split()]


for turn, num in enumerate(mc,1):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num :
                arr[i][j] = 0
            
    
    if bingo_check:
        print(turn)
        break
