def Input():
    arr = [i for i in map(int,input().split())]
    matrix = []
    count = 0
    for i in range(2):
        row = []
        for j in range(3):
            row.append(arr[count])
            count += 1
        matrix.append(row)
    return matrix

def process():
    count = 0
    for i in lst:
        count += sum(i)
    print(count)

lst = Input()
process()