vect = "MINCODING"
n = int(input())
str = input().split()
dat_lst = [0] * len(str)
for i in range(len(str)):
    if str[i] in vect:
        dat_lst[i] += 1

for i in dat_lst:
    if i != 0:
        print("O", end="")
    else:
        print("X", end="")
