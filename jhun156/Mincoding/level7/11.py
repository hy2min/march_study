def custom():
    a = int(input())
    arr = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(a)
            a += 1
        arr.append(row)
    return arr

def output(arr):
    for i in arr:
        for j in i:
            print(j,end = ' ')
        print()

test = custom()
output(test)