import sys
sys.stdin = open('input.txt', 'r')

for test in range(10):
    T = int(input())
    row_lst = [list(input()) for _ in range(100)]
    col_lst = list(map(list, zip(*row_lst)))
    ret = []
    for i in range(100):
        for j in range(100):
            for k in range(0,101):
                slice_str = j+k

                if slice_str > 100:
                    break

                slice_row = row_lst[i][j:slice_str]
                slice_col = col_lst[i][j:slice_str]

                if slice_row == slice_row[::-1]:
                    ret.append(len(slice_row))
                if slice_col == slice_col[::-1]:
                    ret.append(len(slice_col))
    print(f'#{T} {max(ret)}')
