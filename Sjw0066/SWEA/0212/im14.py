
def bingo():
    cnt_bingo=0

    #가로

    for i in range(5):
        cnt=0
        for j in range(5):
            if bingo_arr[i][j] == -1:
                cnt +=1
        if cnt ==5 :
            cnt_bingo += 1

    #세로
    for i in range(5):
        cnt=0
        for j in range(5):
            if bingo_arr[j][i] == -1:
                cnt+=1
        if cnt == 5:
            cnt_bingo += 1
    #대각
    cnt=0
    for i in range(5):
        if bingo_arr[i][i] == -1:
            cnt +=1
    if cnt ==5 :
        cnt_bingo += 1

    cnt=0
    for i in range(5):
        if bingo_arr[i][4-i] ==-1:
            cnt+=1
    if cnt >=5 :
        cnt_bingo += 1

    if cnt_bingo>=3:
        return True
    else:
        return False



arr=[list(map(int,input().split())) for _ in range(5)]
answer=[list(map(int,input().split())) for _ in range(5)]
bingo_arr=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
bingo_answer=0

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if answer[i][j] == arr[k][l]:
                    bingo_arr[k][l] = -1
                    bingo_answer += 1
                    break

            if bingo():
                break
        if bingo():
            break
    if bingo():
        break
print(bingo_answer)









