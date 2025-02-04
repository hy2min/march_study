vect = ['B','T','K','I','G','Z']
target = input().split()

cnt = 0
for s in target:
    if s in vect:
        cnt += 1

print(cnt)