st = input()
st1 = st[:len(st)//2]
st2 = st[len(st)//2:]
if st1 == st2 : 
    print('동일한문장')
else : 
    print('다른문장')
