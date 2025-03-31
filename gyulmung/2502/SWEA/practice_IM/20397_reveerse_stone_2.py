import sys # 35분
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for j in range(M):
        y, x = map(int, input().split())
        y -= 1
        for k in range(1, x + 1):
            left = y - k
            right = y + k
            if left < 0 or right > N - 1:
                break
            elif arr[left] == 1:
                if arr[left] == arr[right]:
                    arr[left] = 0
                    arr[right] = 0
            elif arr[left] == 0:
                if arr[left] == arr[right]:
                    arr[left] = 1
                    arr[right] = 1
    print(f'#{i}',*arr)
