
arr = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]

def getSum() :
    startindex = int(input())
    sum = 0

    for i in range(startindex, startindex +5) :
        sum += arr[i]
    print(sum)
    

getSum()