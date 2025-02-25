s = input()
s = s.upper()
p = s.count('PASS')
f = s.count('FAIL')

ret = (p / (p+f)) * 100
print(f'{int(ret)}%')