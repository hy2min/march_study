vect = ['B','T','K','I','G','Z']
target = [i for i in input().split()]
cnt = 0
for i in vect:
    for j in target:
        if i == j:
            cnt += 1
print(cnt)