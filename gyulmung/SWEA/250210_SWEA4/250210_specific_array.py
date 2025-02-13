import sys
sys.stdin = open('input.txt', 'r')

test = int(input())

for i in range(1, test +1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 정렬진행
    for j in range(0, N - 1):
        for k in range(j+1, N):
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
    # 각 자리에 삽입
    lst = []
    for l in range(5):
        lst.append(arr[N-1-l])
        lst.append(arr[l])

    print(f'#{i}', *lst)
