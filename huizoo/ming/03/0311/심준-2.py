arr = [list(map(int, input().split())) for _ in range(3)]
a = input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
while arr != arr2:
    arr = [list(row) for row in list(zip(*arr))[::-1]]
    cnt += 1

print(cnt)
