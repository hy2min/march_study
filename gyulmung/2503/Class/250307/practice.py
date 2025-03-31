A, B = map(int,input().split())
answer = 0
gcd = 0
a, b = A, B
while b:
    answer = a%b
    a = b
    b = answer
gcd = a

lcm = ((A//gcd)*(B//gcd))*gcd
print(gcd, lcm)