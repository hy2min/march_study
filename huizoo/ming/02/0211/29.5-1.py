n = int(input())
jumping = ['시작', 3, 1, 2, 1 ,3, 2, 1, 2, 1, '도착']

def jump(x):
    print(jumping[x], end=' ')
    if jumping[x] == '도착':
        return
    if jumping[x] == '시작':
        next_jump = n   
    else :
        next_jump = jumping[x]
    jump(x + next_jump)
    print(jumping[x], end=' ')

jump(0)