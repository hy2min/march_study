T = int(input())
for idx in range(T):
    arr = []
    for _ in range(5):
        arr.append(list(map(str, input())))
    max_len = len(max(arr, key=lambda x: len(x)))
    word = ""
    for j in range(max_len): # 열
        for i in range(5):  # 행
            if j >= len(arr[i]):
                continue
            else:
                word += arr[i][j]
    print(f'#{idx+ 1} {word}')
