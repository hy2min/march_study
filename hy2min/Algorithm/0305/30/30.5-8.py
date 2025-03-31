n = int(input())
arr = ['B','I','A','H']
# ans = []
# si = 0
# while arr:
#     idx = (si+n-1) % len(arr)
#     ans.append(arr.pop(idx))
#     si = idx
# print(*ans)
idx = 0
while arr:
    idx = (idx + n) % len(arr) -1
    print(arr.pop(idx))