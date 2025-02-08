st = 'ATKPTCABC'
a, b = input().split()
reversed_st = st[::-1]
length = len(st) - st.index(a) - reversed_st.index(b) - 1
print(length)