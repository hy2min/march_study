T = int(input())
for idx in range(T):
    sudoku = []
    num_lst = list(range(1, 10))

    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    flag = 1

    #행 체크
    for i in range(9):
        row = sorted(sudoku[i])
        if row != num_lst:
            flag = 0
            break
        # 열 체크
    for i in range(9):
        column = []
        for j in range(9):
            column.append(sudoku[j][i])
        column = sorted(column)
        if column != num_lst:
            flag = 0
            break

    for i in range(3):
        square = []
        for j in range(3):
            square.extend(sudoku[j][3*i:3*(i+1)])
        square = sorted(square)
        if square != num_lst:
            flag = 0
            break
    print(f'#{idx+1} {flag}')
