a,b,c = input().split()

if ord(a) >= ord(b) and ord(a) >= ord(c):
    print(f"옳다{a}")
else:
    print("옳지않음")