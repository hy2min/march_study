alp_list = list(input())
alp_cnt = [0] * 26
for alp in alp_list:
    alp_cnt[ord(alp)-65] += 1

for i in range(26):
    if alp_cnt[i] == max(alp_cnt):
        print(chr(i+65))


        ord("A") = 65
