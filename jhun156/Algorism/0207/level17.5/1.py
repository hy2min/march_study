arr = [3,4,1,1,2,6,8,7,8,9,10]

def getSum(index):
    result = 0
    for i in range(index,index+5):
        result += arr[i]
    return result

a = int(input())
ans = getSum(a)
print(ans)