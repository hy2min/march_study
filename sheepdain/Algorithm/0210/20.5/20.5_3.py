a=input()
n=len(a)//2
if a[:n] == a[n:]:
    print('동일한문장')
else:
    print('다른문장')