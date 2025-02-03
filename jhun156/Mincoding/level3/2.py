a,b = map(int,input().split())

if a > b:
    print(f"큰수는 {a}")
elif a < b:
    print(f"큰수는 {b}")
else:
    print("같은숫자")