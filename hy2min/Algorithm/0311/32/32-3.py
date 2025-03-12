n = int(input())
arr = list(map(int, input().split()))

stack = []
for i in arr:
    if stack and stack[-1][0] == i:
        stack[-1][1] += 1
        if stack[-1][1] == 3:
            stack.pop()
    else:
        stack.append([i,1])

ans = []
for i in stack:
    ans += [i[0] for _ in range(i[1])]
ans.sort()

print(*ans)