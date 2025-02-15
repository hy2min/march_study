st = input()
length = len(st)
if st[:length//2] == st[length//2:]:
    print('동일한문장')
else:
    print('다른문장')