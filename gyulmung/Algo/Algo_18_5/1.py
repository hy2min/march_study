arr = [['G', 'K', 'G'], list(map(str, input().split()))]
lst = [0]*26

for i in range(2):
    for j in range(3):
        lst[ord(arr[i][j]) - 65] += 1

Flag = False
for i in range(len(lst)):
    if lst[i] >= 3:
        Flag = True

if Flag:
    print('있음')
else:
    print('없음')
