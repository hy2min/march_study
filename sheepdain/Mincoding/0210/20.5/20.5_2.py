a=input()
a_l=len(a)
for i in range(a_l):
    for j in range(a_l-i-1,a_l):
        print(a[j],end='')
    print()