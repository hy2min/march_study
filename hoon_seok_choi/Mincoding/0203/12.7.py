a1 = input()
a = input()
b = input()
c = input()

len = 0

for _ in a1 :
    len += 1
    if len  > 10 :
        break

def counting(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

cnt1 = counting(a1,a)
print(f"{a}={cnt1}")
cnt2 = counting(a1,b)
print(f"{b}={cnt2}")
cnt3 = counting(a1,c)
print(f"{c}={cnt3}")

