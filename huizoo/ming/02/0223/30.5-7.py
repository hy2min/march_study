# nums = list(map(int, input().split()))
# cnt = 0
# path = []
# path2 = []
# def dfs(Sum):
#     global cnt
#     if Sum>20:
#         return
#     if 10<=Sum<=20:
#         Set = set(path)
#         if Set not in path2:
#             path2.append(Set)
#             cnt+=1
#     for num in nums:
#         if num not in path:
#             path.append(num)
#             dfs(Sum+num)
#             path.pop()
# dfs(0)
# print(cnt)

def dfs(n, Sum):
    global cnt
    if Sum > 20:
        return
    elif 10 <= Sum <= 20:
        cnt += 1

    for i in range(n, length):
        dfs(i + 1, Sum + nums[i])


nums = list(map(int, input().split()))
length = len(nums)
cnt = 0
# path = []
# combine = []
dfs(0, 0)
print(cnt)