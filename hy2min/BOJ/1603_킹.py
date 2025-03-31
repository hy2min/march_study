
move = {
    'R':(0,1),
    'L':(0,-1),
    'B':(1,0),
    'T':(-1,0),
    'RT':(-1,1),
    'LT':(-1,-1),
    'RB':(1,1),
    'LB':(1,-1)
}

king, stone, n = input().split()
king_y = 8-int(king[1])
king_x = ord(king[0])-65
stone_y = 8-int(stone[1])
stone_x = ord(stone[0])-65
n = int(n)


for _ in range(n):
    di, dj = move[input()]
    ni, nj = king_y+ di, king_x + dj
    if 0 <= ni < 8 and 0 <= nj < 8:
        if stone_y == ni and stone_x == nj:
            ei,ej = stone_y+di, stone_x+dj
            if 0 <= ei < 8 and 0 <= ej < 8:
                stone_y,stone_x = ei,ej
                king_y,king_x = ni,nj
        else:
            king_y,king_x = ni,nj

print(f'{chr(king_x+65)}{8-king_y}')
print(f'{chr(stone_x+65)}{8-stone_y}')