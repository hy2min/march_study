arr = [['G', 'K', 'G']]
arr.append(input().split())
alp_list = [0] * 26
for alps in arr:
    for alp in alps:
        alp_list[ord(alp)-54] += 1
flag = 0
for i in range(26):
    if alp_list[i] >= 3:
        flag = 1
        break
if flag:
    print("있음")
else:
    print("없음")
