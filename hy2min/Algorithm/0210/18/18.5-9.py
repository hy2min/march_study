alp = input()
dat_lst = [0] * 26
for i in alp:
    if dat_lst[ord(i) - 65] == 0:
        dat_lst[ord(i) - 65] = 1

for i in range(len(dat_lst)):
    if dat_lst[i] == 1:
        print(chr(i + 65), end="")
