s= input()
forbiden_words = ['bad','no','puck']

flag = 1
# 1.싫어하는 단어 존재
for word in forbiden_words:
    if word in s:
        flag = 0
        break

# 2._개수 5개 이하
if '_____' in s:
    flag = 0

#각알파벳 사용횟수 5개 이하
alp_count = {}
for char in s:
    if char.isalpha():
        if char in alp_count:
            alp_count[char] += 1
        else:
            alp_count[char] = 1
        if alp_count[char] > 5:
            flag = 0
            break

# 4.숫자가 없어야 함
for i in s:
    if i.isdigit(): 
        flag = 0
        break

if flag:
    print('pass')
else:
    print('fail')