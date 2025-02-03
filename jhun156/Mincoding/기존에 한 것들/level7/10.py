a = input()

def custom():
    global a
    arr = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(a)
        arr.append(row)
    return arr

def output(test_arr):
    for i in test_arr:
        for j in i:
            print(j,end='')
        print()

test = custom()
output(test)