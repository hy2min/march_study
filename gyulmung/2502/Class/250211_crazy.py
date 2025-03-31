lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

# 7*7 배열
# A는 5칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# B는 3칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# '#'은 벽이다
# 벽 그리고 A,B 뒤로는 물풍선이 터지지 않는다.

# 물을 피할곳은 지도상 몇군데인가? - 16 -

# import sys
# sys.stdin = open('input.txt', 'r')
#


def water_balm(y, x):
    global lst
    directY = [-1, 1, 0, 0]
    directX = [0, 0, -1, 1]
    A = 5
    B = 3

    if lst[y][x] == 'A':
        for i in range(4):
            for j in range(1, A + 1):
                dy = y + (directY[i] * j)
                dx = x + (directX[i] * j)
                if dy >= 7 or dx >= 7 or dy < 0 or dx < 0:
                    continue
                elif lst[dy][dx] == '#' or lst[dy][dx] == 'A' or lst[dy][dx] == 'B':
                    break
                else:
                    lst[dy][dx] = 1

    elif lst[y][x] == 'B':
        for i in range(4):
            for j in range(1, B + 1):
                dy = y + (directY[i] * j)
                dx = x + (directX[i] * j)
                if dy >= 7 or dx >= 7 or dy < 0 or dx < 0:
                    continue
                elif lst[dy][dx] == '#' or lst[dy][dx] == 'A' or lst[dy][dx] == 'B':
                    continue
                else:
                    lst[dy][dx] = 1

count = 0
for i in range(7):
    for j in range(7):
        if lst[i][j] == 'A' or lst[i][j] == 'B':
            water_balm(i, j)
        if lst[i][j] == '_':
            count += 1
print(lst)
print(count)