arr = [i for i in map(int,input().split())]

DAT = [0] * 10

for i in range(len(arr)):
    DAT[arr[i]] += 1

flag = False
for i in range(10):
    if DAT[i] >= 2:
        flag = True

if flag == True:
    print("도플갱어 발견")
else:
    print("미발견")