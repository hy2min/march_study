lst_pass = [3,7,4,9]
arr = [i for i in map(int,input().split())]

def isSame(k, num):
    if lst_pass[k] == num:
        return 1
    return 0

ans = 0
for i in range(4):
    a = isSame(i,arr[i])
    ans += a

if ans == 4:
    print('pass')
else:
    print('fail')