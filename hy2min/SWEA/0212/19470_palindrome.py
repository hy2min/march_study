T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))

    for i in range(N):
        for j in range(N-M+1):
            string = matrix[i][j:j + M]
            if string == string[::-1]:
                print(f'#{idx+1} {"".join(string)}')

    for i in range(N):
        for j in range(N-M+1):
            string = []
            for x in range(M):
                string.append(matrix[j+x][i])
            if string == string[::-1]:
                print(f'#{idx + 1} {"".join(string)}')


