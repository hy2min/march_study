def fib(i):
    gma.append(gma[-1] + gma[-2])
    if i == n:
        print(gma[n])
        return
    fib(i+1)

n = int(input())
if n >1:
    gma = [0, 1]
    fib(2)
else:
    print(n)