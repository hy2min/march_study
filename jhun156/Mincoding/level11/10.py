arr = [
    [3,2,6,2,4],
    [1,4,2,6,5],
]

def MAIN():
    target = int(input())
    result = KFC(target)
    if result == 1:
        print("값이 존재합니다")
    else:
        print("값이 없습니다")

def KFC(number):

    global arr

    for i in range(2):
        rnt = arr[i].count(number)
        if rnt > 0:
            return 1 
    return 0

MAIN()