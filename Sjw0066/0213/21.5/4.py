arr=[list(input()) for _ in range(4)]

answer=[["_"]*3 for _ in range(4)]
def gravity(y,x):
    cnt=0
    for i in range(1,4):
        ny=y+i
        if ny>3:
            continue
        if arr[ny][x] != "_": #아래 있는 글자 세기
            cnt+=1
    if cnt:
        answer_y=3-cnt
        answer[answer_y][x] = arr[y][x]
    else:
        answer[3][x] = arr[y][x]

for i in range(4):
    for j in range(3):
        if arr[i][j] != '_':
            gravity(i,j)

for i in answer:
    for j in i:
        print(j,end="")
    print()
