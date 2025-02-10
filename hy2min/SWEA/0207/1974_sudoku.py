T = int(input())
for idx in range(T):
    sudoku = []
    num_lst = [i for i in range(1, 10)]

    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    flag = 1
    for i in range(9):
        check_sudoku = []
        for j in range(9): # 열 체크
            check_sudoku.append(sudoku[i][j])
            if num_lst != sorted(check_sudoku):
                flag = 0
                break
    for i in range(9): # 행 체크
        if num_lst != sorted(check_sudoku):
            flag = 0
            break

    for i in range(3):
        for j in range(3):
            check_sudoku.append(sudoku[3*i][3*j])
