def dfs(row):
    global mx_score

    if row == n:
        score = col_sum(arr)
        if mx_score < score:
            mx_score = score
        return

    for k in range(n):
        rotate(row,k)
        dfs(row+1)



def rotate(row, k):
    k = k % n
    arr[row] = arr[row][-k:] + arr[row][:-k]
    return

def col_sum(arr):
    score = 1
    for j in range(n):
        column = 0
        for i in range(n):
            column += arr[i][j]
        score *= column
    return score

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mx_score = -21e8
dfs(0)
print(f'{mx_score}점')
