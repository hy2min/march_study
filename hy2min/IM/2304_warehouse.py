N = int(input())
lst = []

for _ in range(N):
    L, H = map(int, input().split())
    lst.append((L,H))
lst.sort()

max_height = -1
max_index = -1

for i in range(N):
    if lst[i][1] > max_height:
        max_height = lst[i][1]
        max_index = i

area = 0

# 왼쪽
left_h = lst[0][1]
left_idx = lst[0][0]
for i in range(max_index):
    if lst[i+1][1] > left_h:
        area += left_h * (lst[i+1][0] - lst[i][0])
        left_h = lst[i+1][1]
    else:
        area += left_h * (lst[i+1][0] - lst[i][0])


# 최대 높이
area += max_height

# 오른쪽
right_h = lst[-1][1]

for i in range(N-1, max_index, -1):
    if lst[i-1][1] > right_h:
        area += right_h * (lst[i][0] - lst[i-1][0])
        right_h = lst[i-1][1]
    else:
        area += right_h * (lst[i][0] - lst[i-1][0])

print(area)