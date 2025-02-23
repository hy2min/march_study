arr = [
    [10, 20],
    [30, 60],
    [100, 150],
    [200, 300]
]


cal = list(map(int,input().split()))

lev0 = 0
lev1 = 0
lev2 = 0
lev3 = 0

for i in range(6) :
    if arr[0][0] <= cal[i] <= arr[0][1] :
        lev0 +=1
    if arr[1][0] <= cal[i] <= arr[1][1] :
        lev1 +=1
    if arr[2][0] <= cal[i] <= arr[2][1] :
        lev2 +=1
    if arr[3][0] <= cal[i] <= arr[3][1] :
        lev3 +=1

cnt_arr = [lev0,lev1,lev2,lev3]


for i in range(4) :
    print(f"lev{i}:{cnt_arr[i]}")
