from collections import deque

T = 10
for idx in range(10):
    n = int(input())
    arr = deque(list(map(int, input().split())))
    flag = 1
    while True:

        for i in range(1,6):
            a = arr.popleft()-i

            if a <= 0:
                a = 0
                arr.append(a)
                flag = 0
                break

            arr.append(a)


        if flag == 0:
            break

    print(f'#{idx+1}', *arr)
