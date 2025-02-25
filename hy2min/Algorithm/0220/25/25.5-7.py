def good_name(s):
    vowel_cnt = 0
    char = {}
    if not s.islower() or not s.isalpha():
        return 'no'
    for i in s:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1

        if char[i] > 2:
            return 'no'
    for i in s:
        if i in vowel:
            vowel_cnt += 1
        
    if vowel_cnt != 3:
        return 'no'
    return 'good'

n = int(input())

vowel = ['a','e','i','o','u']
for _ in range(n):
    s = input()
    print(good_name(s))