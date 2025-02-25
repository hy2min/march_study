arr = [3,4,1,1,2,6,8,7,8,9,10]

def getSum():
    startIndex = int(input())
    total = 0   
    for i in range(startIndex, startIndex + 5):
        total += arr[i]
    return total

print(getSum())