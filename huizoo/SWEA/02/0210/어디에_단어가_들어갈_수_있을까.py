t = int(input())
def find_word(arr, key):
    cnt = 0
    for i in range(n):
        for j in range(n-k+1):
            if arr[i][j:j+k] == key:
                if 0 <= j-1 and j+k < n:
                    if arr[i][j-1] == '0' and arr[i][j+k] == '0':
                        cnt += 1
                elif j-1 < 0 and arr[i][j+k] == '0':
                    cnt += 1
                elif n <= j+k and arr[i][j-1] == '0':
                    cnt += 1
    return cnt

for tc in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [''.join(input().split()) for _ in range(n)]
    word = '1'*k
    ans = find_word(puzzle, word)
    puzzle = list(zip(*puzzle))
    for i in range(n):
        puzzle[i] = ''.join(puzzle[i])
    ans += find_word(puzzle, word)
    print(f'#{tc} {ans}')