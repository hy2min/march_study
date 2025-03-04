

for i in range(10):
    tc=int(input())
    row_list=[list(input()) for _ in range(100)]
    col_list=list(map(list,zip(*row_list)))

    cnt=0
    for i in range(100):
        for j in range(100):
            for k in range(j+1,101):
                slice_row = row_list[i][j:k]
                slice_col = col_list[i][j:k]

                if slice_row == slice_row[::-1]:
                    if len(slice_row)>cnt:
                        cnt=len(slice_row)
                        
                if slice_col == slice_col[::-1]:
                    if len(slice_col)>cnt:
                        cnt=len(slice_col)
    
    print(f'#{tc} {cnt}')
                