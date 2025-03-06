# 7*7 배열
# A는 5칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# B는 3칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# '#'은 벽이다
# 벽 그리고 A,B 뒤로는 물풍선이 터지지 않는다.

# 물을 피할곳은 지도상 몇군데인가? - 16 -

lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def boom(y, x, power):
    for i in range(4):
        for p in range(1, power + 1):
            ny, nx = y + dy[i]*p, x + dx[i]*p
            if 0 <= ny < 7 and 0 <= nx < 7:
                if lst[ny][nx] == '#' or lst[ny][nx] == 'A' or lst[ny][nx] == 'B':
                   break
                else: lst[ny][nx] = 'X'


for y in range(7):
    for x in range(7):
        if lst[y][x] == 'A':
            boom(y, x, 5)
        if lst[y][x] == 'B':
            boom(y, x, 3)
cnt = 0
for i in range(7) :
    for j in range(7) :
        if lst[i][j] == '_' :
            cnt += 1
print(cnt)