t = int(input())
for tc in range(1, t+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(0, 2*E, 2):
        if left[arr[i]]:
            right[arr[i]] = arr[i+1]
        else:
            left[arr[i]] = arr[i+1]
    cnt = 0
    def bst(x):
        global cnt
        if x:
            cnt+=1
            bst(left[x])
            bst(right[x])

    bst(N)
    print(f'#{tc} {cnt}')