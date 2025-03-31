arr = [tuple(map(int, input().split())) for _ in range(3)]

if arr[0][0] == arr[1][0] or arr[1][0] == arr[2][0] or arr[0][0] == arr[2][0]:
    print('위험')
elif arr[0][1] == arr[1][1] or arr[1][1] == arr[2][1] or arr[0][1] == arr[2][1]:
    print('위험')
else:
    print('안전')
