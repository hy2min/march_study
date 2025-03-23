numbers = list(map(int, input().split()))
dat = [0]*10
for num in numbers : 
    dat[num] += 1
if max(dat) >= 2 : 
    print("도플갱어 발견")
else : 
    print("미발견")