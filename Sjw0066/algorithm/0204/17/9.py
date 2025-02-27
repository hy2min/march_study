vect=[[3,7,4],[2,2,4],[2,2,5]]

target=list(map(int,input().split()))

dat=[0]*8


for i in range(3):
    for j in range(3):
        for k in range(3):
            if vect[i][j] == target[k] :
                dat[vect[i][j]] += 1
            

max_cnt=max(dat)
max_num=dat.index(max_cnt)

print(max_num)