alp_list = list(input())
alp_cnt = [0] * 25
for alp in alp_list:
    alp_cnt[ord(alp)-65] += 1

for i in range(25):
    if alp_cnt[i] == max(alp_cnt):
        print(chr(i+65))