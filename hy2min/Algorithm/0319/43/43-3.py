dic = {}
arr = 'BOBOOBOBOBOBBM'
for i in range(len(arr)-2):
    if arr[i:i+3] in dic:
        dic[arr[i:i+3]] += 1
    else:
        dic[arr[i:i+3]] = 1

n = int(input())
for _ in range(n):
    key = input()
    print(dic[key])
