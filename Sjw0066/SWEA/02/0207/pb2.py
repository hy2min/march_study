
T= int(input())

for tc in range(1, T + 1):
    N=int(input())
    paint=[list(map(int,input().split())) for _ in range(N)]

    arr=[[0]*10 for _ in range(10)]

    for i in range(len(paint)):
        r1= paint[i][0]
        c1= paint[i][1]
        r2= paint[i][2]
        c2= paint[i][3]
        color= paint[i][4]
        for j in range(r1,r2+1):
            for k in range(c1,c2+1):
                arr[j][k]+=color

    cnt=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3 :
                cnt+=1

    print(f'#{tc} {cnt}')


