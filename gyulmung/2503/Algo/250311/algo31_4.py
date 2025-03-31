import sys
sys.stdin = open('input.txt', 'r')

arr = [list(input()) for _ in range(5)]
for i in range(5):
    arr[i][1], arr[i][3] = arr[i][3], arr[i][1]

Flag = True
for i in range(5):
    arr[i] = ''.join(arr[i])
    if arr[i] == 'MAPOM':
        Flag = False

if Flag:
    print('no')
else:
    print('yes')