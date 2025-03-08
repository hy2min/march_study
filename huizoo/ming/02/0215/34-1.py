arr = [4,4,5,7,8,10,20,22,23,24]
n = int(input())
start = 0
end = len(arr)-1
found = 0
while start <= end:
    mid = (start+end)//2
    if arr[mid] < n:
        start = mid+1
    elif arr[mid] >n:
        end = mid-1
    else:
        found = 1
        break
if found:
    print('O')
else:
    print('X')