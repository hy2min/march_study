arr = list(map(int, input().split()))
n = int(input())
Max = 0
def abc(x, Sum):
    global Max
    if x == n:
        Max = max(Max, Sum)
        return
    food = arr[:]
    for i in range(0, 3):
        one = arr[i]
        arr[i] = 0
        for j in range(3, 6):
            two = arr[j]
            arr[j] = 0
            for k in range(1, 5):
                three = arr[k]
                arr[k] = 0
                abc(x+1)


