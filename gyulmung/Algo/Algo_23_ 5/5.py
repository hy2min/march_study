num = list(map(int, input().split()))

def left():
    Min_i = 0
    for i in range(7, -1, -1):
        if num[0] > num[i]:
            Min_i = i
            return Min_i

def right():
    Max_i = 0
    for i in range(1, 8):
        if num[0] < num[i]:
            Max_i = i
            return Max_i

while True:
    Min = left()
    Max = right()
    if Min < Max:
        num[0], num[Min] = num[Min], num[0]
        break
    num[Min], num[Max] = num[Max], num[Min]


print(*num)