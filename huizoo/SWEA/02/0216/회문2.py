def abc(arr):
    global Max
    for i in range(100):
        for j in range(99):
            for k in range(j, 100):
                if arr[i][j:k+1] == arr[i][j:k+1][::-1]:
                    if Max < k-j+1:
                        Max = k-j+1

for tc in range(1, 11):
    n = input()
    lst = [list(input()) for _ in range(100)]
    Max = 0
    lst2 = list(zip(*lst))
    abc(lst)
    abc(lst2)
    print(f'#{tc} {Max}')