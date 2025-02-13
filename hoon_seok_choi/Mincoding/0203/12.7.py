a1 = input()
a = input()
b = input()
c = input()



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

