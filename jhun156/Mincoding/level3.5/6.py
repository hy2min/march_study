a,b = map(int,input().split())

if a * b > 30 and a * b < 50:
    print("적당한 사이즈")
elif a * b >= 50:
    print("큰 사이즈")
elif a * b <= 30:
    print("작은 사이즈") 