import sys
sys.stdin = open("input.txt", "r")


for tc in range(1, 11):
    N = int(input())
    # 상단은 N극 , 하단은 S극
    # 1 = N극, 2 = S극
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N):
        magnetic = 0
        for i in range(N):
            now = arr[i][j]
            if magnetic == 0 and now == 1:
                magnetic = 1
            elif magnetic == 1 and now == 2:
                magnetic = 0
                cnt += 1

    print(f'#{tc} {cnt}')