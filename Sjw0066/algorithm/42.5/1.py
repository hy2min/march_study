import copy
N=int(input())
cube=[list(map(int,input().split())) for _ in range(N)]
Max=-21e8
used=[0] * N

def turn_cube(arr):
    temp=arr[0]
    for i in range(N-1):
        arr[i] , arr[i+1] = arr[i+1],arr[i]
    arr[0] = temp


def get_sum(arr):
    ret=1
    Sum=0
    for i in range(N):
        for j in range(N) :
            Sum+=arr[j][i]
        ret *= Sum
    return ret

def dfs(level,arr):
    global Max

    if level==(N-1)*N:
        ret=get_sum(arr)
        if Max<ret:
            Max=ret
            return

    temp = copy.deepcopy(arr)
    for i in range(N):
        turn_cube(arr[i])
        dfs(level+1,arr)
        arr=copy.deepcopy(temp)

dfs(0,cube)
print(Max)

