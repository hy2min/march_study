for tc in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    last_ladder = ladder[99]
    y, x = 99, last_ladder.index(2)

    while y > 0:
        if 0 < x <= 98:
            if ladder[y][x - 1] == 1:
                x -= 1
                while ladder[y - 1][x] == 0 :
                    x -= 1
                y -= 1
            elif ladder[y][x + 1] == 1:
                x += 1
                while ladder[y - 1][x] == 0 :
                    x += 1
                y -= 1
            elif ladder[y - 1][x] == 1:
                y -= 1
        elif x == 99:
            if ladder[y][x - 1] == 1:
                x -= 1
                while ladder[y - 1][x] == 0 :
                    x -= 1
                y -= 1
            elif ladder[y - 1][x] == 1:
                y -= 1
        elif x == 0:
            if ladder[y][x + 1] == 1:
                x += 1
                while ladder[y - 1][x] == 0 :
                    x += 1
                y -= 1
            elif ladder[y - 1][x] == 1:
                y -= 1

    print(f'#{tc} {x}')