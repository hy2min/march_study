arr = ['A','F','G','A','B','C']

ablist = list(input().split())
count = 0

for i in ablist:
    for j in arr:
        if i == j:
            count += 1
            break

if count == 2:
    print("와2개")
elif count == 1:
    print("오1개")
else:
    print("우0개")