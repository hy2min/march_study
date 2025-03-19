st = input()
arr = list(st)
n = len(st)
def abc(i, n):
    high = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left <= n - 1 and arr[high] < arr[left]:
        high = left
    if right <= n - 1 and arr[high] < arr[right]:
        high = right
    if high == i:
        return
    arr[i], arr[high] = arr[high], arr[i]
    abc(high, n)

for i in range(n//2-1, -1, -1):
    abc(i, n)
for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    abc(0, i)
print(''.join(arr[::-1]))

