nums = [1, 2, 3, 4, 5]
answer_list = []

def nCr(n, ans, r):
    global count

    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
            # if 10 <= sum(answer_list) <= 20:
            #     count += 1
        return
    ans.append(nums[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)

count = 0
for i in range(len(nums)):
    nCr(0, [], i)
print(answer_list)