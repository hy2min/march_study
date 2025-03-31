import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+2)
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b
    for i in range(N-M, 0, -1):
        arr[i] = arr[2*i +1]+arr[2*i]
    print(f'#{test} {arr[L]}')
