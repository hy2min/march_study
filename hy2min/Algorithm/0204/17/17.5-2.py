arr = [3,7,4,1,2,6]
def isExist():
    univer = []
    for _ in range(2):
        univer.append(list(map(int, input().split())))
    for i in univer:
        for j in i:
            if j in arr:
                print("OK", end=" ")
            else:
                print("NO", end=" ")
        print()

isExist()