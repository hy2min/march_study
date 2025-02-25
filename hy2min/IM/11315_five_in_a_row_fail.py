
def check(arr): # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                cnt = 0

            if cnt >= 5:
                return 1
    return 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[j][i] == 'o':
            cnt += 1
        else:
            cnt = 0
        if cnt == 5:
            return 1

def cross(arr):
    for i in range(N):
        cnt = 0
        for j in range(i+1):
            if arr[j][i-j] == 'o':
                cnt += 1
            else:
                cnt = 0

            if cnt >= 5:
                return 1
    return 0

def cross1(arr):
    for i in range(N):
        cnt = 0
        for j in range(i+1):
            if arr[N-1-i+j][j] == 'o':
                cnt += 1
            else:
                cnt = 0

            if cnt >= 5:
                return 1
    return 0


T = int(input())
for idx in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    arr1 = list(map(list, zip(*arr)))
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 5:



        print(f"#{idx+1} YES")
    else:
        print(f"#{idx+1} NO")

