N = int(input())
data = [input() for _ in range(N)]

start = 0
end = N - 1
i = 0
y, x = -1, -1

while i < N : 
    start = 0
    end = N - 1
    found = 0
    while start <= end : 
        mid = (start + end) // 2
        if data[i][mid] == '#' :
            start = mid + 1
            y, x = i, mid
            found = 1
        else : 
            end = mid - 1
    if not found :
        break
    i += 1

# while start <= end :
#     mid = (start + end) // 2
#     if data[i][mid] == '#' : 
#         start = mid + 1
#         y, x = i, mid
#     else : 
#         end = mid - 1
#     if mid == N - 1 and i < N - 1 : 
#         i += 1
#         start = 0
#         end = N - 1

print(y, x)