# def dfs(n, Sum):
#     global cnt
#     if 10 <= Sum <= 20 and set(path) not in combine:
#         combine.append(set(path))
#         cnt += 1
#     if n == len(nums):
#         return    
#     for i in range(len(nums)):
#         if nums[i] not in path:
#             path.append(nums[i])
#             dfs(n+1, Sum+nums[i])
#             path.pop()
            
def dfs(n, Sum):
    global cnt
    if Sum > 20:
        return
    elif 10 <= Sum <= 20:
        cnt += 1

    for i in range(n, length):
        dfs(i+1, Sum+nums[i])
        
nums = list(map(int, input().split()))
length = len(nums)
cnt = 0
# path = []
# combine = []
dfs(0, 0)
print(cnt)