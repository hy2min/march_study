string = input()
alp_list = [0] * 26
for i in string:
    alp_list[ord(i)-65] += 1

max_alp = alp_list.index(max(alp_list))
print(chr(max_alp+65))
