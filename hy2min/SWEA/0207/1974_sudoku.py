T = int(input())
for idx in range(T):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
