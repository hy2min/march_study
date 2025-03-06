a = [list(map(int, input().split())) for _ in range(3)]
input()
b = [list(map(int, input().split())) for _ in range(3)]

a1 = [row[:] for row in a]
cnt = 0
while True:
    if a == b:
        break
    a = [[a[j][2-i] for j in range(3)] for i in range(3)]
    cnt += 1
print(cnt)