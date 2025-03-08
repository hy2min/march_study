n = int(input())

time = [12, 9, 3, 6]

def rotated(arr):
    rotated_arr = [arr[1], arr[3], arr[0], arr[2]]
    return rotated_arr

for i in range((n//90)%4):
    time = rotated(time)

print(*time)