import sys
sys.stdin = open("input.txt", "r")

def abc(x):
    global Max
    if x == n:
        Max = max(Max, int(''.join(arr)))
        return

    if n%2 == x%2:
        Max = max(Max, int(''.join(arr)))

    for i in range(l):
        for j in range(l):
            if i == j: continue
            arr[i], arr[j] = arr[j], arr[i]
            if (''.join(arr), x%2) not in checked:
                checked.add((''.join(arr), x%2))
                abc(x+1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1, T+1):
    arr, n = input().split()
    n = int(n)
    arr = list(arr)
    l = len(arr)
    checked = set()
    Max = 0
    abc(0)
    checked.add((''.join(arr), 0))
    print(f'#{tc} {Max}')