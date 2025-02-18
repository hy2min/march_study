T= int(input())

for tc in range(1, T + 1):
    N,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]

    def cnt_row():
        result=0
        for i in range(N):
            cnt = 0
            for j in range(N):
                if arr[i][j] == 1:
                    cnt+=1
                if arr[i][j] ==0 or j==N-1:
                    if cnt==K:
                        result +=1
                        cnt = 0
                    else:
                        cnt=0

        return result



    def cnt_col():
        result = 0
        for i in range(N):
            cnt = 0
            for j in range(N):
                if arr[j][i] == 1:
                    cnt += 1
                if arr[j][i] == 0 or j == N - 1:
                    if cnt == K:
                        result += 1
                        cnt=0
                    else:
                        cnt = 0

        return result

    ret1 = cnt_row()
    ret2 = cnt_col()
    answer=ret1+ret2
    print(f'#{tc} {answer}')