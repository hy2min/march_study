n = int(input())

stack = []
for _ in range(n):
    y, x, strength = input().split()
    stack.append(list(map(int,strength)))
wind_n = int(input())
allpower = list(map(int, input().split()))
for i in range(n):
    for power in allpower:
        if not stack[i]:
            break
        elif stack[i] and stack[i][-1] <= power:
            stack[i].pop()
        else:
            stack[i][-1] -= power

cnt = 0

for i in stack:
    for j in i:
        if j:
            cnt += 1
print(cnt)
