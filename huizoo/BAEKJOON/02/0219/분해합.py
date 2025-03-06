N = input()
num = int(N)
len_N = len(N)
# start 가 음수가 되는 것을 방지
start = max(1, num - len_N*9)
Min = 1e9
for i in range(start, num):
    Sum = i
    for j in str(i):
        Sum += int(j)
    if Sum == num:
        Min = min(i, Min)
if Min == 1e9:
    print(0)
else:
    print(Min)