arr = [i for i in input().split()]

count = 0

for i in arr:
    if ord(i) >= ord('0') and ord(i) <= ord('9'):
        count += 1

if count > 0:
    print(f"숫자{count}개발견")
else:
    print("숫자미발견") 