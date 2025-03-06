# n = int(input())
# while n > 1:
#     for i in range(2, n+1):
#         if n%i==0:
#             print(i)
#             n //= i
#             break

n = int(input())
i = 2
while i * i <= n:
    while n % i == 0:
        print(i)
        n //= i
    i += 1

if n > 1:
    print(n)
