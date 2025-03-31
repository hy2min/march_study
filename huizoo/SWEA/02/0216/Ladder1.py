for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    x = arr[99].index(2)
    y = 99
    while y > 0:
        if x != 0 and arr[y][x-1]:
            while x != 0 and arr[y][x-1]:
                x -= 1
            y -= 1
        elif x != 99 and arr[y][x+1]:
            while x != 99 and arr[y][x+1]:
                x += 1
            y -= 1
        else:
            y -= 1
    print(f'#{tc} {x}')