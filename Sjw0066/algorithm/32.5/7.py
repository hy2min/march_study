arr=[list(map(int,input().split())) for _ in range(4)]

def get_sum(y,x):
    st_y=y
    st_x=x
    ed_y=st_y
    ed_x=st_x

    while 1:
        ed_y+=1
        if ed_y > 3:
            break
        if arr[ed_y][st_x]==0:
            break
    while 1:
        ed_x += 1
        if ed_x > 7:
            break
        if arr[st_y][ed_x] == 0:
            break
    Sum=0
    for i in range(st_y,ed_y):
        for j in range(st_x,ed_x):
            if arr[i][j] :
                Sum+=arr[i][j]
            else:
                Sum=0
                return Sum
    return Sum

Max=-21e8
for i in range(4):
    for j in range(8):
        if arr[i][j] :
            ret=get_sum(i,j)
            if Max<ret:
                Max=ret


print(Max)

