model = [['_', '_', '_'],
         ['_', '_', '_'],
         ['A', 'T', 'K'],
         ['_', '_', '_'],
         ['_', '_', '_']]

behave = []
for i in range(7):
    be = list(map(str, input().split()))
    behave.append(be)

ay, ax = 2, 0
ty, tx = 2, 1
ky, kx = 2, 2

for k in range(7):
    if behave[k][0] == 'A':
        if behave[k][1] == "UP":
            model[ay][ax], model[ay - 1][ax] = model[ay - 1][ax], model[ay][ax]
            ay -= 1
        elif behave[k][1] == 'DOWN':
            model[ay][ax], model[ay + 1][ax] = model[ay + 1][ax], model[ay][ax]
            ay += 1
        elif behave[k][1] == 'RIGHT':
            model[ay][ax], model[ay][ax + 1] = model[ay][ax + 1], model[ay][ax]
            ax += 1
        elif behave[k][1] == 'LEFT':
            model[ay][ax], model[ay][ax - 1] = model[ay][ax - 1], model[ay][ax]
            ax -= 1
    elif behave[k][0] == 'T':
        if behave[k][1] == "UP":
            model[ty][tx], model[ty - 1][tx] = model[ty - 1][tx], model[ty][tx]
            ty -= 1
        elif behave[k][1] == 'DOWN':
            model[ty][tx], model[ty + 1][tx] = model[ty + 1][tx], model[ty][tx]
            ty += 1
        elif behave[k][1] == 'RIGHT':
            model[ty][tx], model[ty][tx + 1] = model[ty][tx + 1], model[ty][tx]
            tx -= 1
        elif behave[k][1] == 'LEFT':
            model[ty][tx], model[ty][tx - 1] = model[ty][tx - 1], model[ty][tx]
            tx += 1
    elif behave[k][0] == 'K':
        if behave[k][1] == "UP":
            model[ky][kx], model[ky - 1][kx] = model[ky - 1][kx], model[ky][kx]
            ky -= 1
        elif behave[k][1] == 'DOWN':
            model[ky][kx], model[ky + 1][kx] = model[ky + 1][kx], model[ky][kx]
            ky += 1
        elif behave[k][1] == 'RIGHT':
            model[ky][kx], model[ky][kx + 1] = model[ky][kx + 1], model[ky][kx]
            kx += 1
        elif behave[k][1] == 'LEFT':
            model[ky][kx], model[ky][kx - 1] = model[ky][kx - 1], model[ky][kx]
            kx -= 1
for i in model:
    print(*i, sep = '')











# def runway(y, x):
#     global model
#     dy = y
#     dx = x
#     for i in range(7):
#         if behave[i][0] == model[dy][dx]:
#             if behave[i][1] == 'UP':
#                 dy += 1
#             elif behave[i][1] == 'DOWN':
#                 dy -= 1
#             elif behave[i][1] == 'RIGHT':
#                 dx += 1
#             elif behave[i][1] == 'LEFT':
#                 dx += 1
#     return dy, dx