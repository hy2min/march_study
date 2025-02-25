arr = [
    ['G','K','G'],
    [i for i in input().split()],
]

DAT = [0] * 100
for i in range(2):
    for j in range(3):
        DAT[ord(arr[i][j])-65] += 1

flag = False
for i in range(100):
    if DAT[i] >= 3:
        flag = True

if flag == True:
    print("있음")
else:
    print("없음")