from copy import deepcopy

def dfs(lst, level):
    global Max
    if level == 5:
        for i in range(N):
            for j in range(N):
               Max = max(Max, lst[i][j])
        return

    for i in range(4):
        temp_lst = move(deepcopy(lst), i)
        dfs(temp_lst, level+1)


def move(lst, dir):
    if dir == 0:    #동
        for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if lst[i][j]:
                    tmp = lst[i][j]
                    lst[i][j] = 0
                    if lst[i][top] == 0:
                        lst[i][top] = tmp
                    elif lst[i][top] == tmp:
                        lst[i][top] = tmp*2
                        top -= 1
                    else:
                        top -= 1
                        lst[i][top] = tmp
    elif dir == 1:  #서
        for i in range(N):
            top = 0
            for j in range(1, N):
                if lst[i][j]:
                    tmp = lst[i][j]
                    lst[i][j] = 0
                    if lst[i][top] == 0:
                        lst[i][top] = tmp
                    elif lst[i][top] == tmp:
                        lst[i][top] = tmp*2
                        top += 1
                    else:
                        top += 1
                        lst[i][top] = tmp
    elif dir == 2:  #남
        for j in range(N):
            top = N-1
            for i in range(N-2, -1, -1):
                if lst[i][j]:
                    tmp = lst[i][j]
                    lst[i][j] = 0
                    if lst[top][j] == 0:
                        lst[top][j] = tmp
                    elif lst[top][j] == tmp:
                        lst[top][j] = tmp*2
                        top -= 1
                    else:
                        top -= 1
                        lst[top][j] = tmp
    else:           #북
        for j in range(N):
            top = 0
            for i in range(1, N):
                if lst[i][j]:
                    tmp = lst[i][j]
                    lst[i][j] = 0
                    if lst[top][j] == 0:
                        lst[top][j] = tmp
                    elif lst[top][j] == tmp:
                        lst[top][j] = tmp*2
                        top += 1
                    else:
                        top += 1
                        lst[top][j] = tmp

    return lst

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = 0

dfs(arr, 0)
print(Max)
