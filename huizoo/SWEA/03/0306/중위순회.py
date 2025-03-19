import sys
sys.stdin = open('input.txt', 'r')


def abc(i):
    if i > N:
        return
    if type(arr[i]) is str:
        print(arr[i], end='')
    else:
        abc(int(arr[i][1]))
        print(arr[i][0], end='')
        if len(arr[i]) == 3:
            abc(int(arr[i][2]))

for tc in range(1, 11):
    N = int(input())
    arr = [0]*(N+1)
    for i in range(1, N+1):
        temp = list(input().split())
        if len(temp) == 2:
            arr[i] = temp[1]
        else:
            arr[i] = tuple(temp[1:])
    print(f'#{tc}', end=' ')
    abc(1)
    print()