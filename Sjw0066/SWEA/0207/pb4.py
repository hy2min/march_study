T= int(input())

for tc in range(1, T + 1):

    arr=[list(map(int,input().split())) for _ in range(9)]

    #set 없이
    def check_row():
        for i in range(9):
            s = 0
            for j in range(9):
                s+=arr[i][j]
            if s!=45:
                return False
        return True

    def check_col():

        for i in range(9):
            s=0
            for j in range(9):
                s+=arr[j][i]
            if s!=45:
                return False
        return True

    def check_box():
        for i in range(0,9,3):
            s = 0
            for j in range(3):
                for k in range(3):
                    s += arr[i+j][i+k]
            if s!=45:
                return False

        return True

    ret1=check_row()
    ret2=check_col()
    ret3=check_box()

    print(f'#{tc} {int(ret1&ret2&ret3)}')


