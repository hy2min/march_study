# def rec(x, n):
#     if x == 0:
#         print(1)
#         return
#     if x == 1:
#         print(n)
#         return
#     rec(x-1, n*x)

def rec1(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    ret = rec1(x-1)
    return x*ret

N = int(input())
# rec(N, 1)
print(rec1(N))