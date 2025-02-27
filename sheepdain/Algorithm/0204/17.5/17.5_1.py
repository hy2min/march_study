arr=[3,4,1,1,2,6,8,7,8,9,10]

def getSum(i):
    s=0
    for j in range(i,i+5):
        s+=arr[j]
    return s

startindex=int(input())
print(getSum(startindex))