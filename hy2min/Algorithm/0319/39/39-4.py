n = int(input())
stick = 100
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for i in arr:
    if stick < i:
        break
    stick -= i
    cnt += 1
print(cnt)