def binary_search(arr,N) :


    start = 0
    end = N-1
    col = -1


    #탐색목표 1 : 숫자가 존재하는 열을 찾는다

    while start <= end :
        mid = (start + end) // 2

        if arr[mid][0] == '#' and arr[mid][N - 1] == '0' :
            col = mid
            break

        if arr[mid][0] == '0':
            end = mid - 1
        else:
            start = mid + 1


    # 탐색목표 2 : 숫자가 존재하는 열 중에서 마지막으로 문자가 쓰인 좌표를 찾는다
    start = 0
    end = N-1
    row = -1


    while start <= end :
        mid = (start + end) // 2

        if arr[col][mid] == '0' and arr[col][end] == '0' :
            row = mid -1
            break

        elif arr[col][mid] == '0' :
            start = mid - 1
        else:
            arr[col][mid] == '#'
            start = mid + 1
            
    return col, row


N = int(input())
arr = [list(input().strip()) for _ in range(N)]

i,mid = binary_search(arr,N)
print(i,mid,end=" ")