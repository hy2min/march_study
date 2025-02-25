arr = [3,4,1,1,2,6,8,7,8,9,10]
def getSum(lst, start_index) : 
    return sum(lst[start_index:start_index+5])

ret = getSum(arr, int(input()))
print(ret)