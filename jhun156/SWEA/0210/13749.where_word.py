# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(arr[i][j])
        lst.append(row)
    for j in range(N):
        row = []
        for i in range(N):
            row.append(arr[i][j])
        lst.append(row)
    # lst = N * N matrix를 가로열, 세로열로 전부 가로열로 만든 2N * N matrix

    def find_K(arr):
        result = 0
        for i in range(N-K+1):
            Sum = 0
            for j in range(K):
                Sum += arr[i+j]
            if Sum == K:
                if 0 < i < N - K and arr[i+K] == 0 and arr[i-1] == 0:
                    result += 1
                elif i == N - K and arr[N-K-1] == 0:
                    result += 1
                elif i == 0 and arr[i+K] == 0:
                    result += 1
        return result
    # 함수 안에 답이 될수 있는 경우의 수 전부 포함
    # 가능한 경우마다 1을 더하고 최종적으로 result 반환

    Sum = 0
    for i in range(2*N):
        ans = find_K(lst[i])
        Sum += ans
    # Sum에 모든 가능한 경우를 더함

    print(f"#{tc} {Sum}")
