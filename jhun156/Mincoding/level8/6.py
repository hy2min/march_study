def Input():

    arr = []    
    a = int(input())

    for i in range(3):
        row = []
        for j in range(4):
            row.append(a)
            a += 1
        arr.append(row)
    
    return arr

def process(arr):

    for i in range(3):
        for j in range(4):
            arr[i][j] += 1

    return arr

def output(arr):

    for i in arr:
        for j in i:
            print(j,end = ' ')
        print()

lst = Input()
test = process(lst)
output(test)