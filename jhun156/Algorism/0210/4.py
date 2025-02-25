# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [list(input()) for _ in range(N)]

def parametric_y_search():
    st = 0
    ed = N - 1
    ans = 0
    while True:
        mid = (st + ed) // 2
        if arr[mid][0] == "#":
            ans = mid
            st = mid + 1
        elif arr[mid][0] == "0":
            ed = mid - 1
        if st > ed:
            break
    return ans

def parametric_x_search(y):
    st = 0
    ed = N - 1
    ans = 0
    while True:
        mid = (st + ed) // 2
        if arr[y][mid] == "#":
            ans = mid
            st = mid + 1
        elif arr[y][mid] == "0":
            ed = mid - 1
        if st > ed:
            break
    return ans

y = parametric_y_search()
x = parametric_x_search(y)
print(y,x)
