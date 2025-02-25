def find_word(arr):
    word_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):

            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == M:
                    word_cnt += 1
                cnt = 0
        if cnt == M:
            word_cnt += 1
    return word_cnt

T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))

    res = find_word(arr) + find_word(arr2)
    print(f'#{idx+1} {res}')
