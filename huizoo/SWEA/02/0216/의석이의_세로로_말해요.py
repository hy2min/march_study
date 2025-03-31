t = int(input())
for tc in range(1, t+1):
    arr = [list(input()) for _ in range(5)]
    Max = max(arr, key=len)
    for i in range(5):
        if len(arr[i]) < len(Max):
            for _ in range(len(Max) - len(arr[i])):
                arr[i].append('')
    arr2 = list(zip(*arr))
    ans = "".join("".join(row) for row in arr2)
    print(f'#{tc} {ans}')
