import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 화물 무게
    arr = list(map(int, input().split()))
    # M개의 트럭 적재용량
    arr2 = list(map(int, input().split()))

    arr.sort(reverse=True)
    arr2.sort(reverse=True)

    cnt = 0
    i = j = 0
    while i < N and j < M:
        if arr2[j] >= arr[i]:
            cnt += arr[i]
            i += 1
            j += 1
        else:
            i += 1

    print(f'#{tc} {cnt}')
