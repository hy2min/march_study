import copy

def trun_right(arr,level):

    if level==K:
        return  arr
    temp=copy.deepcopy(arr)

    for i in range(N):
        for j in range(N):
            temp[j][N-i-1] = arr[i][j]

    ret=trun_right(temp,level+1)

    return ret

N,K=map(int,input().split())
img=[list(map(int,input().split())) for _ in range(N)]

ans=trun_right(img,0)
for i in ans:
    print(*i)