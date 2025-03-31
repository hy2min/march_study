arr = [3, 5, 4, 2]
beat = list(map(int, input().split()))

Sum = 0
for i in range(len(beat)):
    if beat[i] == 1:
        Sum += arr[i]
print(Sum)