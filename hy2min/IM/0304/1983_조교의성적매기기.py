score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        arr.append(a*0.35+b*0.45+c*0.2)

    sort_arr = sorted(arr, reverse=True)
    f = sort_arr.index(arr[k-1])
    ans = score[f//(n//10)]
    print(f'#{tc} {ans}')