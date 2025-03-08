arr = [list(input()) for _ in range(3)]
found = 0
for i in range(3):
    if 'M' in arr[i]:
        found = 1
if found:
    print('M이 존재합니다')
else:
    print('M이 존재하지 않습니다')