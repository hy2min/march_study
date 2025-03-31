arr = [3, 7, 4, 9]
Input = list(map(int, input().split()))

def isSame():
    count = 0
    for i in range(4):
        if arr[i] == Input[i]:
            count += 1
    return count

count = isSame()

if count == 4:
    print('pass')
else:
    print('fail')