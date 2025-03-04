import sys
sys.stdin = open('input.txt', 'r')
T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]

    answer=0

    def find_row():
        max_len=0
        for i in range(N):
            cnt=0
            for j in range(M):
                if a[i][j]:
                    cnt+=1
                    if cnt>max_len:
                        max_len=cnt
                else:
                    if cnt>max_len:
                        max_len=cnt
                    cnt=0

        return max_len


    def find_col():
        max_len = 0
        for i in range(M):
            cnt = 0
            for j in range(N):
                if a[j][i]:
                    cnt += 1
                    if cnt > max_len:
                        max_len = cnt
                else:
                    if cnt > max_len:
                        max_len = cnt
                    cnt = 0

        return max_len

    ret1,ret2=find_row(),find_col()
    if ret1>ret2:
        answer=ret1
    else:
        answer=ret2

    print(f'#{tc} {answer}')