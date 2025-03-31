arr = list(map(int,input().split()))

arr2 = [[0]*3 for _ in range(2)]
a=0
for i in range(2) :
    for j in range(3) :
        arr2[i][j] = arr[a]
        a+=1

min_v = min(arr)
max_v = max(arr)

b = arr.index(min_v)
c= arr.index(max_v)

min_x, min_y = b//3, b%3
max_x, max_y = c//3, c%3

print(f"({max_x},{max_y})")
print(f"({min_x},{min_y})")

