arr = [list(input()) for _ in range(4)]

lst = [
    ['A','B','C','D'],
    ['B','B','A','B'],
    ['C','B','A','C'],
    ['B','A','A','A'],
]

A = B = C = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] == lst[i][j] == 'A':
            A += 1
        elif arr[i][j] == lst[i][j] == 'B':
            B += 1
        elif arr[i][j] == lst[i][j] == 'C':
            C += 1

ans = [A,B,C]
if ans[0] == max(ans):
    print("A")
elif ans[1] == max(ans):
    print("B")
else:
    print("C")