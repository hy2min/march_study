def find_string(lst):
    n = 2
    while n <= 100:
        for i in range(100):
            for j in range(100):
                if lst[i][j:j+n] == lst[i][j:j+n][::-1]:
                    n += 1
                    break
        return n

for _ in range(10):
    idx = int(input())
    matrix = [list(input()) for _ in range(100)]
    matrix2 = list(zip(*matrix))
    max_n = max(find_string(matrix), find_string(matrix2))
    print(f'#{idx+1} {max_n}')
