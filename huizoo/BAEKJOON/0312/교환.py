import sys
input = sys.stdin.readline

def abc(level):
    global Max
    if level == b:
       Max = max(Max, int(''.join(arr)))
       return
    for i in range(n):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            if (''.join(arr), level) in checked or arr[0] == '0':
                arr[i], arr[j] = arr[j], arr[i]
                continue
            checked.add((''.join(arr), level))
            abc(level+1)
            arr[i], arr[j] = arr[j], arr[i]


a, b = input().split()
n = len(a)
arr, b = list(a), int(b)
Max = 0
checked = set()
if n == 1:
    print(-1)
else:
    abc(0)
    if Max == 0:
        print(-1)
    else:
        print(Max)

