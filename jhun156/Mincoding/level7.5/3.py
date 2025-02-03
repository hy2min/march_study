a,b = input().split()

if a.isupper() and b.isupper():
    print("대문자들")
elif a.isupper() or b.isupper():
    print("대소문자")
else:
    for i in range(ord('a'),ord('z')+1):
        print(chr(i),end='')