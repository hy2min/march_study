def main():
    arr = [[0]*3 for _ in range(3)]
    Magic(arr)
    Output(arr)


def Magic(arr):
    count = 1
    for i in range(3):
        for j in range(3):
            if j + i < 3:
                arr[i][j+i] = count
                count += 1
    return arr

def Output(arr):
    for i in range(3):
        for j in range(3):
            print(arr[i][j] if arr[i][j] != 0 else ' ', end = '')
        print()

main()