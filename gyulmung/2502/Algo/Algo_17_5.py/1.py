arr = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]

startIndex = int(input())

def getSum(Index):
    Sum = 0
    for i in range(Index, Index + 5):
        Sum += arr[i]
    return Sum
print(getSum(startIndex))