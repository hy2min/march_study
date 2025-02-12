arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6],
]

lst = list(zip(arr[0],arr[1],arr[2]))
ans = []
for i in range(4):
    ans.append(sum(lst[i]))
index = int(input())
print(ans[index])