import copy
N=int(input())
cube=[list(map(int,input().split())) for _ in range(N)]
Max=-21e8
used=[0] * N

def turn_cube(arr,i):

    temp=arr[i][N-1]

    for j in range(N-1,0,-1):
        arr[i][j] = arr[i][j-1]
    arr[i][0] = temp

    return arr

def get_sum(arr):
    mul=1
    for i in range(N):
        Sum = 0
        for j in range(N):
            Sum+=arr[j][i]
        mul*=Sum
    return mul

def dfs(arr,level):
    global Max

    ret = get_sum(arr)
    if Max < ret:
        Max = ret

    if used==[N-1]*N:
        return

    if level==(N-1)**2:
        return

    temp=copy.deepcopy(arr)

    for i in range(N):
        if used[i] == N-1: continue
        used[i] += 1
        arr2=turn_cube(arr,i)
        dfs(arr2,level+1)
        used[i] -= 1
        arr=copy.deepcopy(temp)


dfs(cube,0)
print(f'{Max}점')




