a = input()
b = input()

a = [*a]
b = [*b]

if a == b :
    print('동명')
for i in range(len(a)) :
    if a[i] != b[i] :
        print('남남')
        break
