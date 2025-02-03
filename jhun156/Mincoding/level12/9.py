a = input()

arr = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
count = 6
moment = 0

if a.isupper():
    for i in range(3):
        for j in range(0,moment+3):
            arr[2-i][j] = 7-count
            count -= 1
        moment -=1
elif 0 <= int(a) <= 9:
    for i in range(3):
        for j in range(moment,3):
            arr[i][j] = count
            count -= 1
        moment += 1

for i in arr:
    for j in i:
        if j == 0:
            print(" ", end = '')
        else:
            print(j,end = '')
    print()