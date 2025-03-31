m, n = map(int, input().split())
cut = int(input())
width = [0,n]
height = [0,m]
for _ in range(cut):
    direction, line = map(int, input().split())
    if direction == 0:
        width.append(line)
    elif direction == 1:
        height.append(line)
width.sort()
height.sort()
max_width = -21e8
max_height = -21e8
for i in range(1, len(width)):
    if width[i]-width[i-1] > max_width:
        max_width = width[i]-width[i-1]
for i in range(1, len(height)):
    if height[i]-height[i-1] > max_height:
        max_height = height[i]-height[i-1]
ans = max_width * max_height
print(ans)