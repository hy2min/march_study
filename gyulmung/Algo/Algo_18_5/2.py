arr = list(map(int, input().split()))
lst = [0]*10

for i in range(6):
    lst[arr[i]] += 1

Flag = True
for i in range(10):
    if lst[i] >= 2:
        Flag = False

if Flag:
    print('미발견')
else:
    print('도플갱어 발견')