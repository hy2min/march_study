def row_check():
    row_word = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    row_word += 1
                    cnt = 0
                else:
                    cnt = 0
    return row_word

def column_check():
    column_word = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    column_word += 1
                    cnt = 0
                else:
                    cnt = 0
    return column_word

T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    row_count = row_check()
    column_count = column_check()
    word_cnt = row_count + column_count
    print(f'#{idx+1} {word_cnt}')



