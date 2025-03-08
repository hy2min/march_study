arr = input()
start = 0
end = len(arr)-1
battery = -1
while start <= end:
    mid = (start+end)//2
    if arr[mid] == '#':
        battery = mid
        start = mid+1
    elif arr[mid] == '_':
        end = mid-1

print((battery+1)*10, '%', sep='')