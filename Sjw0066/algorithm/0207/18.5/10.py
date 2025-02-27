dat=[0] * 100

str_lst=list(input())

for i in str_lst:
    dat[ord(i)] += 1

for i in range(len(dat)):
    if dat[i]:
        print(f'{chr(i)}:{dat[i]}')