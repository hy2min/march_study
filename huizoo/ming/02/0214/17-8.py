arr = ['B','T','K','I','G','Z']
target = input().split()
cnt = 0
for char in target:
    flag = 0
    for i in range(6):
        if arr[i] == char:
            flag = 1
    if flag:
        cnt += 1
print(cnt)
