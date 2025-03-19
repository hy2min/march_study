t = int(input())
for tc in range(1, t+1):
    a, b = input().split()
    n = len(a)
    arr, b = list(a), int(b)
    Max = 0
    checked = set()
    def abc(level):
        global Max
        if level == b:
           Max = max(Max, int(''.join(arr)))
           return
        for i in range(n):
            for j in range(i+1, n):
                arr[i], arr[j] = arr[j], arr[i]
                if (''.join(arr), level) in checked:
                    arr[i], arr[j] = arr[j], arr[i]
                    continue
                checked.add((''.join(arr), level))
                abc(level+1)
                arr[i], arr[j] = arr[j], arr[i]

    abc(0)
    print(f'#{tc} {Max}')