import sys
sys.stdin = open('sample_input(2).txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    total = 0
    idx = 0

    for i in truck:
        while idx < n and weight[idx] > i:
            idx += 1
        if idx < n:
             total += weight[idx]
             idx += 1
    print(f'#{tc} {total}')