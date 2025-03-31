T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    for i in arr:
        if len(i) < max_len:
            while len(i) < max_len:
                i.append(0)

    print(f'#{tc}',end=" ")
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] == 0:
                continue
            print(arr[j][i],end="")
    print()
