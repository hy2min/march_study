arr = [list(input()) for _ in range(5)]
def abc():
    for i in range(5):
        arr[i][1], arr[i][3] = arr[i][3], arr[i][1]
        if ''.join(arr[i]) == 'MAPOM':
            print('yes')
            return
    print('no')
    return

abc()