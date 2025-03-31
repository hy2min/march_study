arr = [list(input()) for _ in range(5)]
for i in range(5):
    arr[i][1], arr[i][3] = arr[i][3], arr[i][1]


for char in arr:
    if "".join(char) == 'MAPOM':
        print('yes')
        break
else:
    print('no')