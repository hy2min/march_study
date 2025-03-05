a = int(input())
arr = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]
used = [0]*6
used[a] = 1
Sum = 0

def dfs(num):

    global Sum
    print(num,Sum)
    for i in range(6):
        if arr[num][i] != 0 and used[i] == 0:
            used[i] = 1
            Sum += arr[num][i]
            dfs(i)

dfs(a)