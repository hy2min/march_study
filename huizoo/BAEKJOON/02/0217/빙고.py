def isBingo(arr):
    bingo = 0
    for row in arr:
        if row.count('O') == 5:
            bingo += 1
    for row in zip(*arr):
        if row.count('O') == 5:
            bingo += 1
    temp1 = 0
    temp2 = 0
    for i in range(5):
        if arr[i][i] == 'O':
            temp1+=1
        if arr[i][4-i] == 'O':
            temp2+=1
    if temp1 == 5:
        bingo += 1
    if temp2 == 5:
        bingo += 1
    return bingo

arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
Bingo = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        found = 0
        for k in range(5):
            for l in range(5):
                if arr2[i][j] == arr1[k][l]:
                    arr1[k][l] = 'O'
                    found = 1
                    break
            if found:
                break
        Bingo = isBingo(arr1)
        if Bingo >= 3:
            break
    if Bingo >= 3:
        break
print(cnt)