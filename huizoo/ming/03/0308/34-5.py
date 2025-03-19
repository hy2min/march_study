n = int(input())
start = 0
end = n
mid = 0
while start <= end:
    mid = (start+end)//2
    if mid**2 > n:
        end = mid-1
    elif mid**2 < n:
        start = mid + 1
    else:
        break
print(end)