arr = input()
ghost = "GHOST"
dat_lst = [0] * 26
for i in arr:
    dat_lst[ord(i) - 65] += 1

flag = 0
for i in ghost:
    if dat_lst[ord(i) - 65] > 0:
        flag = 1
    else:
        flag = 0
        break

if flag:
    print("존재")
else:
    print("존재하지 않음")
