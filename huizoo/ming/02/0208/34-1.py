arr = [4,4,5,7,8,10,20,22,23,24]
n = int(input())
def binary_search(target, data) : 
    start = 0
    end = len(data)-1
    while start <= end : 
        mid = (start+end)//2
        if data[mid] == target:
            return 'O'
        elif data[mid] > target : 
            end = mid - 1
        else :
            start = mid + 1
    return 'X'

ret = binary_search(n, arr)
print(ret)