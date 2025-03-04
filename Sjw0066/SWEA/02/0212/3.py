T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    row_lst=[list(input()) for _ in range(N)]
    col_lst=list(map(list,zip(*row_lst)))

    answer=[]
    for i in range(N):
        for j in range(N):
            slice_index=j+M

            if slice_index>N:
                break

            slice_row = row_lst[i][j:slice_index]
            slice_col = col_lst[i][j:slice_index]

            if slice_row == slice_row[::-1]:
                answer = slice_row
            if slice_col == slice_col[::-1]:
                answer = slice_col

    print(f'#{tc}',end=" ")
    for i in answer:
        print(i,end="")
    print()