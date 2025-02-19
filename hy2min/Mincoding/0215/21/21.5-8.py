location = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['A','T','K'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]
def action(m,act):
    for i in range(5):
        for j in range(3):
            if location[i][j] == m:
                if act == 'UP' and i > 0:
                    location[i-1][j], location[i][j] = location[i][j], location[i-1][j]
                elif act == 'DOWN' and i < 4:
                    location[i+1][j], location[i][j] = location[i][j], location[i+1][j]
                elif act == 'LEFT' and j > 0:
                    location[i][j-1], location[i][j] = location[i][j], location[i][j-1]
                elif act == 'RIGHT' and j < 2:
                    location[i][j+1], location[i][j] = location[i][j], location[i][j+1]

for _ in range(7):
    m, act = input().split()
    action(m,act)

for i in location:
    for j in i:
        print(j, end="")
    print()