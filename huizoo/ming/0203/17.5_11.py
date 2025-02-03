arr = [3,5,4,2]
bit = list(map(int, input().split()))
total = 0
for i in range(4) : 
    if bit[i] : 
        total += arr[i]
print(total)