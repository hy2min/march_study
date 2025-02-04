arr=[3,1,9],[7,2,1],[1,0,8]
masking=[]
for i in range(3):
    masking.append(list(map(int,input().split())))
def Find(M):
    for i in range(3):
        for j in range(3):
            if M[i][j]==1:
                if 3<=arr[i][j]<=5:
                    return print('발견')
    return print('미발견')
Find(masking)