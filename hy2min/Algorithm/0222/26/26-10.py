
def safe_castle(arr):
    for i in range(4):
        for j in range(3):
            if arr[j][i] > arr[j+1][i]:
                print('안전하지않은성')
                return
    print('안전한성')
    return

arr = [
    [0,0,0,0],
    [0,1,1,0],
    [2,2,3,0],
    [1,3,3,1],
]

safe_castle(arr)