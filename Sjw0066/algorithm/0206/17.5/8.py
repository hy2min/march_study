map1=[[3,55,42],[-5,-9,-10]]

pix=[list(map(int,input().split())) for _ in range(2)]

for i in range(2):
    for j in range(2):
        flag=0
        for k in range(2):
            for g in range(3):
                if pix[i][j] == map1[k][g]:
                    flag=1
        if flag==1:
            print("Y",end=" ")
        else:
            print("N",end=" ")
    print()