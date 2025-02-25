arr = input()
dat_lst = [0] * 26

for i in arr:
    dat_lst[ord(i) -65] += 1

for i in range(len(dat_lst)):
    if dat_lst[i] > 0:
        print(f'{chr(i+65)}:{dat_lst[i]}')
