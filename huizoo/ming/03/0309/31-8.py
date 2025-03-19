P = int(input())
N = int(input())
for _ in range(4):
    P = int(str(P*2)[::-1])
print(P)