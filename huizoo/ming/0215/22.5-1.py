arr = [
    [['A','T','B'],['C','C','B']],
    [['A','A','A'],['B','B','C']],
]
a = input()
found = 0
for i in range(2):
    for j in range(2):
        for k in range(3):
            if arr[i][j][k] == a:
                found = 1
                break
        if found: break
    if found: break
if found: print('발견')
else: print('미발견')