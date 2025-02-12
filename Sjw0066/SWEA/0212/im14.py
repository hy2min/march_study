arr=[list(map(int,input().split())) for _ in range(5)]
answer=[list(map(int,input().split())) for _ in range(5)]
bingo_arr=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
def bingo():
    cnt_bingo=0
    cnt = 0
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
    if cnt ==5 :
        cnt_bingo += 1

    return cnt_bingo

bingo_answer=0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if answer[i][j] == arr[k][l]:
                    bingo_arr[k][l] = -1
                    bingo_answer += 1
                    break

                n= bingo()
                if n == 3 :

                    break
            if n == 3:
                break
        if n == 3:
            break
    if n == 3:
        break

print(bingo_answer)










