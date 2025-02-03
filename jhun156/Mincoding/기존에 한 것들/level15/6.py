a = input()
frog = True
for i in range(len(a)-1):
    if a[i].isupper() == a[i+1].isupper():
        frog = False
        break
print("개구리문장" if frog else "일반문장")