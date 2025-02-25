arr = [input() for _ in range(3)]
dat_lst = [0] * 26
for string in arr:
    for i in string:
        dat_lst[ord(i)-65] += 1

for i in dat_lst:
    if i > 1:
        print("No")
        break
else:
    print("Perfect")
