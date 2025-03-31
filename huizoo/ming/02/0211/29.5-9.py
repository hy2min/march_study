st1 = input()
st2 = input()

min_st = min(st1, st2, key=len)
max_st = max(st1, st2, key=len)

longest = ''

for i in range(len(min_st)):
    for j in range(i, len(min_st)):
        if min_st[i:j] in max_st : 
            if len(longest) < len(min_st[i:j]):
                longest = min_st[i:j]

print(longest)