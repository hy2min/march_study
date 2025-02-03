a = input()
b = input()
mod_a = ''

for i in reversed(range(len(a))):
    mod_a += a[i]

if mod_a == b:
    print("거울문장")
else:
    print("거울문장아님")