st1 = input()
st2 = input()
long = max(st1, st2, key=len)
short = min(st1, st2, key=len)
max_st = ''
for i in range(len(short)-1):
    for j in range(i+1, len(short)):
        if short[i:j] in long:
            max_st = max(short[i:j], max_st, key=len)

print(max_st)