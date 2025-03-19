def abc():
    for i in range(5):
        for j in range(2):
            if SOS.get(arr[i][j:j+4]):
                print('yes')
                return
    print('no')


SOS = {
    '1011': 1,
    '0011': 1,
    '1111': 1,
    '0000': 1,
    '1100': 1,
}

arr = [input() for _ in range(5)]

abc()