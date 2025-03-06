def abc(lst):
    global cnt
    for i in range(N):
        for j in range(N-K+1):
            temp = 0
            for k in range(K):
                if lst[i][j+k] == 1:
                    temp += 1
            if temp == K:
                if j == 0 and lst[i][j+K] == 0:
                    cnt+=1
                elif 0<j<N-K and lst[i][j-1] == 0 and lst[i][j+K] == 0:
                    cnt+=1
                elif j == N-K and lst[i][j-1] == 0:
                    cnt+=1

t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))
    cnt = 0
    abc(arr)
    abc(arr2)
    print(f'#{tc} {cnt}')