# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)] # 확인할 스도쿠
    ans_lst = [0] * 18
    flag = True

    def Sum_matrix(y,x):
        result = arr[y][x]
        directX = [0,0,1,-1,1,1,-1,-1]
        directY = [1,-1,0,0,1,-1,1,-1]
        for i in range(8):
            dy = y + directY[i]
            dx = x + directX[i]
            result += arr[dy][dx]
        return result

    for i in range(9):
        for j in range(9):
            ans_lst[i] += arr[i][j]
            ans_lst[i+9] += arr[j][i]
    for i in range(1,8,3):
        for j in range(1,8,3):
            tmp = Sum_matrix(i,j)
            ans_lst.append(tmp)
    for i in range(27):
        if ans_lst[i] != 45:
            flag = False
            break

    if flag:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")