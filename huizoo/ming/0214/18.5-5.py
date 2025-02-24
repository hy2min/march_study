st = 'ATKPTCABC'
a, b = input().split()
print(abs(-st.index(a) + len(st) - st[::-1].index(b) - 1))