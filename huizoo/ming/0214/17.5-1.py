arr = [3,4,1,1,2,6,8,7,8,9,10]
n = int(input())
def getsum(n):
    return sum(arr[n:n+5])
print(getsum(n))