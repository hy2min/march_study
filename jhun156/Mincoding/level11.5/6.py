arr =[
    ['a','b','E'],
    ['E',2,'W'],
    [3,2,4],
]

for i in range(3):
    for j in range(3):
        if type(arr[i][j]) is int:
            print(arr[i][j]+5,end = ' ')
        else:
            if arr[i][j].islower():
                print(arr[i][j].upper(),end = ' ')
            else:
                print(arr[i][j].lower(),end = ' ')
    print()