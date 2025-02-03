arr = [i for i in input().split()]
count = 0
test = 0

for i in arr:
    test = i.isupper()
    if test == True:
        count += 1

if count == 3:
    print("풍족하다")
elif count == 1 or count == 2:
    print("적절하다")
else:
    print("부족하다")