arr=[[3,5,9],[4,2,1],[1,1,5]]

arr2=[list(map(int,input().split())) for _ in range(3)]

answer=0
for i in range(3):
    for j in range(3):
        if arr2[i][j] == 1 :
            answer+=arr[i][j]

print(answer)    

